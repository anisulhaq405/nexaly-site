/* ============================================================
   NexalyPlanner AI — Cloudflare Worker (FREE, no API key needed)
   Uses Cloudflare Workers AI (Llama). Multilingual + human tone.
   Receives { messages, catalogue } from the site widget and
   returns { reply }. See SETUP guide for how to deploy.
   ============================================================ */
export default {
  async fetch(request, env) {
    const cors = {
      "Access-Control-Allow-Origin": "*",              // or set to "https://nexalyplanner.com"
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };
    if (request.method === "OPTIONS") return new Response(null, { headers: cors });
    if (request.method !== "POST")
      return new Response("POST only", { status: 405, headers: cors });

    try {
      const body = await request.json();
      const messages = Array.isArray(body.messages) ? body.messages : [];
      const catalogue = String(body.catalogue || "");

      const system =
        "You are Nexaly Assistant, the warm, friendly, human support assistant for NexalyPlanner (nexalyplanner.com), an online store. " +
        "Sound like a real, helpful support person — natural, kind and concise. Never sound robotic. Use short sentences and, when useful, a short bullet list. " +
        "VERY IMPORTANT: always reply in the SAME language the customer writes in (detect it automatically). " +
        "Only talk about NexalyPlanner and the REAL products and guides listed in the catalogue below. Never invent products, prices, features or links. " +
        "When a customer describes a need, recommend the best-fit product(s): give the product name, its price, one short reason it fits, and its link. " +
        "Explain how the products work when asked: they are interactive HTML apps that run in the browser, work fully offline, are a one-time purchase (no subscription), keep data private on the customer's own device, and are an instant digital download. " +
        "If you don't know a specific detail, say so warmly and point them to the product page, /faq/, /contact/ or /refund/. " +
        "Keep replies focused and genuinely helpful. If a request is vague, ask one friendly clarifying question.\n\n" +
        catalogue;

      // keep the last ~12 turns to stay fast
      const chat = [{ role: "system", content: system }, ...messages].slice(-13);

      const out = await env.AI.run("@cf/meta/llama-3.3-70b-instruct-fp8-fast", {
        messages: chat,
        max_tokens: 700,
        temperature: 0.5,
      });

      const reply =
        (out && (out.response || (out.result && out.result.response))) || "";

      return new Response(JSON.stringify({ reply }), {
        headers: { ...cors, "Content-Type": "application/json" },
      });
    } catch (err) {
      return new Response(JSON.stringify({ reply: "", error: String(err) }), {
        status: 500,
        headers: { ...cors, "Content-Type": "application/json" },
      });
    }
  },
};
