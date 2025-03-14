document.getElementById("radioForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const selected = document.querySelector('input[name="color"]:checked');
    alert(selected ? selected.value : "No option selected");
  });


  document.getElementById("checkboxForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const checkboxes = document.querySelectorAll('input[name="hobby"]:checked');
    const values = Array.from(checkboxes).map(cb => cb.value);
    alert(values.length ? values.join(", ") : "No option selected");
  });


  document.getElementById("selectForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const selected = document.querySelector('select[name="fruit"]').value;
    alert(selected);
  });

  console.log(true && false); // false
console.log(true || false); // true
console.log(!true); // false
console.log(5 > 4 && 11 < 20); // true
console.log(4 > 10 || 9 < 20); // true
