(() => {
  const pad = (n, len) => String(n).padStart(len, "0");

  const DigitRoll = class {
    constructor(el, val) {
      this.el = el;
      this.val = String(val);
      this.boxes = [];
      this.render();
    }

    render() {
      this.el.innerHTML = "";
      this.boxes = [];
      for (const ch of this.val) {
        const box = document.createElement("span");
        box.className = "digit-box";
        box.innerHTML = `<span class="num">${ch}</span>`;
        this.el.appendChild(box);
        this.boxes.push(box);
      }
    }

    update(newVal) {
      const s = String(newVal);
      if (s.length !== this.val.length) {
        this.val = s;
        this.render();
        return;
      }
      for (let i = 0; i < s.length; i++) {
        if (s[i] !== this.val[i]) {
          const box = this.boxes[i];
          const oldNum = box.querySelector(".num:not(.leave)");
          const newNum = document.createElement("span");
          newNum.className = "num enter";
          newNum.textContent = s[i];
          oldNum.classList.add("leave");
          box.appendChild(newNum);
          oldNum.addEventListener("animationend", () => {
            oldNum.remove();
            newNum.classList.remove("enter");
          }, { once: true });
        }
      }
      this.val = s;
    }
  };

  const init = () => {
    const runtimeEl = document.getElementById("runtimeshow");
    const counterEl = document.getElementById("runtime-counter");
    if (!runtimeEl || !counterEl) return;

    const publishDate = runtimeEl.getAttribute("data-publishDate");
    if (!publishDate) return;
    const startTime = new Date(publishDate).getTime();
    if (isNaN(startTime)) return;

    counterEl.style.display = "none";

    const mkSpan = (cls, text) => {
      const s = document.createElement("span");
      if (cls) s.className = cls;
      if (text) s.textContent = text;
      return s;
    };

    const container = mkSpan("runtime-digits");
    const daysGroup   = mkSpan("digit-group");
    const hoursGroup  = mkSpan("digit-group");
    const minsGroup   = mkSpan("digit-group");
    const secsGroup   = mkSpan("digit-group");

    container.appendChild(daysGroup);
    container.appendChild(mkSpan("unit", "天"));
    container.appendChild(hoursGroup);
    container.appendChild(mkSpan("unit", "小时"));
    container.appendChild(minsGroup);
    container.appendChild(mkSpan("unit", "分"));
    container.appendChild(secsGroup);
    container.appendChild(mkSpan("unit", "秒"));

    const sandClock = runtimeEl.querySelector(".sand-clock");
    if (sandClock) sandClock.remove();

    counterEl.insertAdjacentElement("afterend", container);

    const calc = () => {
      const diff = Date.now() - startTime;
      return {
        d: Math.floor(diff / 86400000),
        h: Math.floor((diff / 3600000) % 24),
        m: Math.floor((diff / 60000) % 60),
        s: Math.floor((diff / 1000) % 60),
      };
    };

    const initial = calc();
    const daysRoll  = new DigitRoll(daysGroup, String(initial.d));
    const hoursRoll = new DigitRoll(hoursGroup, pad(initial.h, 2));
    const minsRoll  = new DigitRoll(minsGroup, pad(initial.m, 2));
    const secsRoll  = new DigitRoll(secsGroup, pad(initial.s, 2));

    setInterval(() => {
      const t = calc();
      daysRoll.update(String(t.d));
      hoursRoll.update(pad(t.h, 2));
      minsRoll.update(pad(t.m, 2));
      secsRoll.update(pad(t.s, 2));
    }, 1000);
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
