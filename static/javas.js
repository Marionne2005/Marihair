console.log("fichier javas.js chargé !!");

document.querySelectorAll('.menu a').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    document.body.classList.add('fade-out');
    setTimeout(() => {
      window.location.href = this.href;
    }, 300);  // 300ms ou le même temps que dans le CSS
  });
});

function resetFormFields(formId) {
  const form = document.getElementById(formId);
  if (form) {
    form.reset();
  }
}


function openBooking(name, price) {
  document.getElementById('serviceName').textContent = name;
  document.getElementById('priceService').textContent = 'Price ' + price;
  document.getElementById('bookingModal').style.display = 'flex';
  document.getElementById('service_choice').innerText = "Name of the service : " + name;
  document.getElementById('price').innerText = 'Price : ' + price;

  document.getElementById('hidden_service').value = name;
  document.getElementById('hidden_price').value = price;
}

function openWarning() {
  document.getElementById('warningWindow').style.display = 'flex';
}

function closeBooking() {
  document.getElementById('bookingModal').style.display = 'none';
  document.getElementById('warningWindow').style.display = 'none';
  document.getElementById('newService').style.display = 'none';
  resetFormFields('newService');
}

function continueBooking() {
  document.getElementById('warningWindow').style.display = 'none';
}

function closeWarn() {
  document.getElementById('warningWindow').style.display = 'none';
}

function myfunction() {
  document.getElementById('newService').style.display = 'flex';
}

function openAppointment() {
  document.getElementById("confirmContainer").style.display = "block";
}

function closePage() {
  document.getElementById('confirmContainer').style.display = 'none';
  document.getElementById('pageContainer').style.display = 'none';
}

function closeConfirm() {
  document.getElementById('confirmContainer').style.display = 'none';
  resetFormFields('confirmContainer');
}
