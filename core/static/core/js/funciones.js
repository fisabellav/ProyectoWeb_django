
$(function(){
    mostrarFechaActual();
    clima();
    
});

function mostrarFechaActual(){
    var today = new Date();
    var options = {weekday: 'short', day: 'numeric', month: 'short', year: 'numeric'};

    var fecha = today.toLocaleString('es', options);
    var hora = today.toLocaleTimeString('es');

    var html_hora = `<h5 class="card-title">${hora}</h5>`;
    var html_fecha = `<p class="card-text">${fecha}</p>`;
    $('#hora').html(html_hora);
    $('#fecha').html(html_fecha);
    let tiempo = setTimeout(function() {
        mostrarFechaActual();
    }, 1000);
}

function clima(){
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(position => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            let lang = 'es';
            let units = 'metric';
            let appid = '7e9a3edffcc7742bf9008a5c0b760435';
            let urlClima = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=${units}&lang=${lang}&appid=${appid}`;
            $.getJSON(urlClima, function(dataClima) {
                let icon_url = `https://openweathermap.org/img/wn/${dataClima.weather[0].icon}@2x.png`;
                let desc_clima = dataClima.weather[0].description;
                let html_img = `<img id="icon-clima" class="ms-0" src="${icon_url}" alt="${dataClima.weather[0].description}"/>`;
                let html_temp = `<h5 class="card-title mb-0 mt-auto">${dataClima.main.temp}°C</h5>
                                <p class="card-text">${desc_clima}</p>`;

                $('#temperatura').html(html_temp);
                $('#img-clima').html(html_img);
            });
        });
        
    
    
    } else {
    /* geolocation IS NOT available */
    }
    
}

const darkMode = () => {
    $("body").attr("data-bs-theme", "dark");
    $("#tema-icon").attr("class", "bi bi-sun-fill");
    localStorage.setItem('data-bs-theme', 'dark');
}

const lightMode = () => {
    $("body").attr("data-bs-theme", "light");
    $("#tema-icon").attr("class", "bi bi-moon-fill");
    localStorage.setItem('data-bs-theme', 'light');
}

const cambiarTema = () => {
    $("body").attr('data-bs-theme') === "light"?
    darkMode(): lightMode();
}

$("#btn-theme").on('click', function (){
    cambiarTema();
})

localStorage.getItem('data-bs-theme') === "dark"?
darkMode(): lightMode();



function myMap() {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(position => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            const myLatLng = { lat: lat, lng: lon};
            var mapProp= {
            center:myLatLng,
            zoom:16,
            };
            var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
            var marker = new google.maps.Marker({position: myLatLng, map,});

            marker.setMap(map);
        });
    }
}

apiGatitos();
// Realizar la solicitud a la API de gatitos
function apiGatitos(){
    let urlCats = `https://api.thecatapi.com/v1/images/search`;
    $.getJSON(urlCats, function(data) {
        let url = data[0].url;
        let height = data[0].height;
        let width = data[0].width;
        if (height < 400 && width > 450) {
            let imgGatitos = `<img id="gatito-img" class="img-fluid" src="${url}" alt="imagen gatito"/>`;
            $('#gatitos').html(imgGatitos);
        } else {
            apiGatitos();
        }
    })
    .catch(error => {
    // Manejar el error en caso de que la solicitud falle
    console.error('Error al obtener las imágenes de gatitos:', error);
    });
}
