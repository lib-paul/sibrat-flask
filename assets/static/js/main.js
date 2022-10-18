const btnDelete = document.querySelectorAll(".btn-delete");
const btnConfirmGuardar = document.querySelectorAll(".btn-confirm");


if (btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (!confirm("¿Seguro que quieres eliminar?")) {
        e.preventDefault();
      }
    });
  });
}

if (btnConfirmGuardar) {
  const btnArray = Array.from(btnConfirmGuardar);
  btnArray.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (!confirm("Le faltan algunos componentes a tu armador")) {
        e.preventDefault();
      } else {
      }
    });
  });
}

setTimeout(() => {
  const box = document.getElementById('alert');

  // 👇️ hides element (still takes up space on page)
  box.style.display = 'none';
}, 6800);
