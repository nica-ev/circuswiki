export async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  const text = await response.text();
  let data;
  try {
    data = text ? JSON.parse(text) : null;
  } catch (error) {
    const preview = text.slice(0, 120).replace(/\s+/g, " ");
    throw new Error(
      `Expected JSON from ${path}, got ${response.status} ${response.statusText}: ${preview}`
    );
  }

  if (!response.ok) {
    throw new Error(data?.error || response.statusText);
  }
  return data;
}
