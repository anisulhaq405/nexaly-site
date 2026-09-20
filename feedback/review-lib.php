<?php
declare(strict_types=1);

const NEXALY_PRODUCTS = [
    'boutique-business-planner' => 'Boutique Business Planner',
    'adhd-digital-planner' => 'ADHD Digital Planner',
    'offline-ai-business-copilot' => 'Offline AI Business Copilot',
    'ai-student-planner' => 'AI Student Planner',
    'batchtrace-os' => 'BatchTrace OS',
    'small-business-planner-2026-2028' => 'Small Business Planner 2026–2028',
    'caregiver-planner-aging-parents' => 'Caregiver Planner for Aging Parents',
    'content-marketing-planner' => 'Content Marketing Planner',
    'owneros-core' => 'OwnerOS Core',
    'digital-homeschool-planner' => 'Digital Homeschool Planner',
    'inventory-procurement-planner' => 'Inventory & Procurement Planner',
    'rentflow-os' => 'RentFlow OS',
];

function review_json(array $data, int $status = 200): never {
    http_response_code($status);
    header('Content-Type: application/json; charset=utf-8');
    header('Cache-Control: no-store');
    echo json_encode($data, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
    exit;
}
function review_storage_dir(): string {
    $dir = dirname(__DIR__) . '/private-feedback';
    if (!is_dir($dir) && !mkdir($dir, 0750, true) && !is_dir($dir)) review_json(['ok' => false, 'message' => 'The review service is temporarily unavailable.'], 500);
    return $dir;
}
function review_product(string $slug): string {
    if (!isset(NEXALY_PRODUCTS[$slug])) review_json(['ok' => false, 'message' => 'Unknown product.'], 404);
    return $slug;
}
function review_read_jsonl(string $file): array {
    if (!is_file($file)) return [];
    $rows = []; $handle = fopen($file, 'rb'); if (!$handle) return [];
    flock($handle, LOCK_SH);
    while (($line = fgets($handle)) !== false) { $row = json_decode($line, true); if (is_array($row)) $rows[] = $row; }
    flock($handle, LOCK_UN); fclose($handle); return $rows;
}
function review_write_jsonl(string $file, array $row): bool {
    return file_put_contents($file, json_encode($row, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . PHP_EOL, FILE_APPEND | LOCK_EX) !== false;
}
function review_records(string $product): array {
    $dir = review_storage_dir();
    $records = review_read_jsonl($dir . '/' . $product . '-feedback.jsonl');
    if ($product === 'boutique-business-planner') $records = array_merge(review_read_jsonl($dir . '/boutique-feedback.jsonl'), $records);
    $decisions = review_read_jsonl($dir . '/review-decisions.jsonl'); $latest = [];
    foreach ($decisions as $decision) if (($decision['product'] ?? '') === $product && isset($decision['feedback_id'])) $latest[$decision['feedback_id']] = $decision;
    foreach ($records as &$record) if (isset($latest[$record['id'] ?? ''])) { $record['status'] = $latest[$record['id']]['status']; $record['moderated_at'] = $latest[$record['id']]['created_at'] ?? null; }
    unset($record); return $records;
}
