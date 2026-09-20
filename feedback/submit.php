<?php
declare(strict_types=1);
require_once __DIR__ . '/review-lib.php';
if ($_SERVER['REQUEST_METHOD'] !== 'POST') review_json(['ok' => false, 'message' => 'Method not allowed.'], 405);
$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origin !== '' && !in_array($origin, ['https://nexalyplanner.com', 'https://www.nexalyplanner.com'], true)) review_json(['ok' => false, 'message' => 'Request not allowed.'], 403);
session_start(); $now = time();
$recent = array_values(array_filter($_SESSION['nexaly_feedback_times'] ?? [], static fn($time) => $time > $now - 3600));
if (count($recent) >= 3) review_json(['ok' => false, 'message' => 'Please wait before sending another message.'], 429);
$payload = json_decode(file_get_contents('php://input') ?: '', true); if (!is_array($payload)) $payload = $_POST;
if (trim((string)($payload['website'] ?? '')) !== '') review_json(['ok' => true, 'message' => 'Thank you for your feedback.']);
$product = review_product((string)($payload['product'] ?? $_GET['product'] ?? ''));
$type = (string)($payload['type'] ?? 'suggestion'); if (!in_array($type, ['review', 'suggestion', 'issue', 'comment'], true)) $type = 'suggestion';
$name = trim((string)($payload['name'] ?? '')); $email = trim((string)($payload['email'] ?? '')); $title = trim((string)($payload['title'] ?? '')); $message = trim((string)($payload['message'] ?? ''));
$rating = (int)($payload['rating'] ?? 0); $publishConsent = !empty($payload['publish_consent']);
if (strlen($name) > 80 || strlen($email) > 160 || strlen($title) > 100 || strlen($message) < 5 || strlen($message) > 1500) review_json(['ok' => false, 'message' => 'Please check the information and enter a message between 5 and 1,500 characters.'], 422);
if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) review_json(['ok' => false, 'message' => 'Please enter a valid email address.'], 422);
if ($type === 'review' && ($rating < 1 || $rating > 5)) review_json(['ok' => false, 'message' => 'Please choose a rating from 1 to 5 stars.'], 422);
if ($type !== 'review') { $rating = 0; $publishConsent = false; }
$record = ['id' => bin2hex(random_bytes(8)), 'created_at' => gmdate('c'), 'product' => $product, 'type' => $type, 'rating' => $rating, 'title' => $title, 'name' => $name, 'email' => $email, 'message' => $message, 'publish_consent' => $publishConsent, 'status' => 'pending', 'verified_buyer' => false, 'ip_hash' => hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? '') . '|nexaly-review-v1')];
if (!review_write_jsonl(review_storage_dir() . '/' . $product . '-feedback.jsonl', $record)) review_json(['ok' => false, 'message' => 'Feedback could not be saved right now.'], 500);
$recent[] = $now; $_SESSION['nexaly_feedback_times'] = $recent;
review_json(['ok' => true, 'message' => $type === 'review' ? 'Thank you — your review was sent for approval.' : 'Thank you — your feedback was sent privately to our team.']);
