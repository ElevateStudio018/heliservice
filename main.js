// Öppet-nu-indikator. Vardagar 07–17 (svensk tid).
(function () {
  const el = document.getElementById("status");
  const text = document.getElementById("status-text");
  const parts = new Intl.DateTimeFormat("sv-SE", {
    timeZone: "Europe/Stockholm", weekday: "short", hour: "numeric", hour12: false
  }).formatToParts(new Date());
  const day = parts.find(p => p.type === "weekday").value;
  const hour = parseInt(parts.find(p => p.type === "hour").value, 10);
  const weekday = !["lör", "sön"].some(d => day.startsWith(d));
  const open = weekday && hour >= 7 && hour < 17;

  text.textContent = open ? "Öppet nu · stänger 17:00" : "Stängt just nu · ring eller mejla";
  el.classList.toggle("open", open);
  el.hidden = false;
})();

document.getElementById("year").textContent = new Date().getFullYear();

// Mjuk inglidning när sektioner syns
(function () {
  const items = document.querySelectorAll(".tile, .review, .about-card, .about-copy, .contact-card, .map, .section-head");
  if (!("IntersectionObserver" in window)) return;
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  items.forEach(i => { i.classList.add("reveal"); io.observe(i); });
})();
