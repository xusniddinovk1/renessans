function initMap() {
    // Xaritani markazlashtirmoqchi bo'lgan joyingizning koordinatalarini kiriting
    // Misol: Toshkent markazi koordinatalari
    const location = { lat: 41.2995, lng: 69.2401 }; 
  
    const map = new google.maps.Map(document.getElementById("google-map"), {
        zoom: 15, // Katta qiymat yaqinlashtirilgan ko'rinishni beradi
        center: location,
    });
  
    // Marker qo'shish
    new google.maps.Marker({
        position: location,
        map: map,
        title: "Bizning manzil!"
    });
  }
  
  // Agar Google Maps API skripti oldinroq yuklanmagan bo'lsa,
  // initMap funksiyasini global ob'ektga qo'shamiz.
  // HTML faylida bu allaqachon `callback=initMap` orqali qilingan.
  // Shuning uchun bu yerda qo'shimcha kod shart emas, lekin umumiy holatlar uchun foydali.
  
  // Sahifa yuklanganda xaritani initsializatsiya qilishni ta'minlash uchun:
  // window.onload = initMap; // Bu satrga HTML ichidagi callback yetarli
  