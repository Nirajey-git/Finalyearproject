const weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
const dateid = document.getElementById("id_appointment_date")
const timeid = document.getElementById("id_appointment_time")
const timeidend = document.getElementById("id_appointment_time_end")
const avail = document.getElementById("infodiv")
const bookbtn = document.getElementById("bookbtn")

timeid.setAttribute("step", "60")
timeidend.setAttribute("step", "60")


$('input[type=radio][name=paymentmethod]').on('change', function(e) {
    const val = this.value

    if (val == "stripe") {
        $("#card-element").removeClass("d-none")

    }
})
dateid.addEventListener("change", function(e) {

    const day = weekday[new Date(this.value).getDay()]

    $.ajax({
        type: "post",
        url: $("#form_date").attr("data-url"),
        data: {
            name: day,
            id: $("#form_date").attr("data-doctorid"),
            csrfmiddlewaretoken: $("#form_date").attr("data-csrf")
        },
        success: function(res) {
            const min = res.available_from
            const max = res.available_to
            timeid.min = min
            timeid.max = max
            timeidend.min = min
            timeidend.max = max

            if (min === null || max === null) {
                avail.innerHTML = `<span style="color:#f44;">Not Available in ${res.name}</span>`
                bookbtn.disabled = true
            } else {
                avail.innerText = `${res.name} - Available from ${min} to ${max}`
                bookbtn.disabled = false
            }
        }
    });
})
dateid.min = new Date().toLocaleDateString('en-ca')
var stripe = Stripe('pk_test_51KnF7yK6JtOvnsqJcejQQu5v6v9k9UJnbbS4Wl47vJG5tZibibGwZV8MQl7RU53uWZp6DjgDVnazkrIDccIIp9ry00CR58HIcp');

// Create an instance of Elements.
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};

// Create an instance of the card Element.
var card = elements.create('card', {
    style: style
});

// Add an instance of the card Element into the `card-element` <div>.
card.mount('#card-element');
// Handle real-time validation errors from the card Element.
card.on('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

// Handle form submission.
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    stripe.createToken(card).then(function(result) {
        if (result.error) {
            console.log('sfsfsfsfsfsfsfsfs');
            // Inform the user if there was an error.
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            console.log(result.token);
            // Send the token to your server.
            stripeTokenHandler(result.token);
        }
    });
});

// Submit the form with the token ID.
function stripeTokenHandler(token) {
    // Insert the token ID into the form so it gets submitted to the server
    var form = document.getElementById('payment-form');
    var hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);

    // Submit the form
    form.submit();
}