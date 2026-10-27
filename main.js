// Offertformulär i popup.
// Sätt FORM_ENDPOINT till t.ex. en Formspree-/Web3Forms-adress för att skicka direkt.
// Utan endpoint öppnas besökarens mejlprogram med förfrågan ifylld.
(function () {
  const FORM_ENDPOINT = "";
  const TO = "heliservice@telia.com";

  const dialog = document.getElementById("quote");
  const form = document.getElementById("quote-form");
  const done = document.getElementById("quote-done");
  const doneText = document.getElementById("quote-done-text");
  const error = document.getElementById("quote-error");

  function open() {
    form.hidden = false;
    done.hidden = true;
    error.hidden = true;
    dialog.showModal();
    document.body.classList.add("modal-open");
  }
  function close() { dialog.close(); }

  document.querySelectorAll("[data-open-quote]").forEach(b => b.addEventListener("click", open));
  dialog.addEventListener("click", e => {
    if (e.target === dialog || e.target.closest("[data-close-quote]")) close();
  });
  dialog.addEventListener("close", () => document.body.classList.remove("modal-open"));

  form.addEventListener("submit", async e => {
    e.preventDefault();
    const missing = [...form.querySelectorAll("[required]")].filter(f => !f.value.trim());
    form.querySelectorAll(".invalid").forEach(f => f.classList.remove("invalid"));
    if (missing.length) {
      missing.forEach(f => f.classList.add("invalid"));
      error.textContent = "Fyll i beskrivning, namn och telefon så kan Henrik återkomma.";
      error.hidden = false;
      missing[0].focus();
      return;
    }
    error.hidden = true;

    const d = Object.fromEntries(new FormData(form));
    const subject = `Offertförfrågan: ${d.typ} – ${d.namn}`;
    const body = [
      `Typ av jobb: ${d.typ}`,
      `När: ${d.nar}`,
      "",
      d.beskrivning,
      "",
      `Namn: ${d.namn}`,
      `Telefon: ${d.telefon}`,
      ...(d.epost ? [`E-post: ${d.epost}`] : []),
      ...(d.ort ? [`Ort: ${d.ort}`] : [])
    ].join("\n");

    const btn = form.querySelector('[type="submit"]');
    if (FORM_ENDPOINT) {
      btn.disabled = true;
      try {
        const res = await fetch(FORM_ENDPOINT, {
          method: "POST",
          headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify({ ...d, _subject: subject })
        });
        if (!res.ok) throw new Error(res.status);
        doneText.textContent = "Förfrågan är skickad. Henrik hör av sig.";
      } catch {
        error.textContent = "Något gick fel. Ring 070-628 51 90 så löser vi det.";
        error.hidden = false;
        btn.disabled = false;
        return;
      }
      btn.disabled = false;
    } else {
      location.href = `mailto:${TO}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      doneText.textContent = "Ditt mejlprogram öppnas med förfrågan ifylld. Tryck skicka där så når den Henrik.";
    }
    form.reset();
    form.hidden = true;
    done.hidden = false;
  });
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
