// Stripe payment flow/logic from here: https://stripe.com/docs/payments/accept-card-payments?platform=web&ui=elements

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
const appearance = {
    theme: 'flat',
    variables: {
      colorPrimary: '#000000',
      colorText: '#000000',
    },
  };


var card = elements.create('card', { appearance: appearance });
card.mount('#card-element');


// Handle validation errors on the card
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // Prevents the form from submitting
    ev.preventDefault();
    // Disables the form
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Captures form data that is not in the payment intent
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // Because we are using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    // Send the data to cache_checkout view
    var url = '/checkout/cache_checkout_data/';
    $.post(url, postData).done(function () {
       // Call the confirm card payment method from Stripe 
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address.value),
                        line2: $.trim(form.optional_address.value),
                        city: $.trim(form.city.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address.value),
                    line2: $.trim(form.optional_address.value),
                    city: $.trim(form.city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // Reload the page, the error will be in django messages
        location.reload();
    })
});