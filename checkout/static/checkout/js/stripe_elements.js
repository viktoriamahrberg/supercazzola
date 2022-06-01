var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card', {appearance: appearance});

var appearance = {
    theme: 'flat',
    variables: {
      fontWeightNormal: '500',
      borderRadius: '2px',
      colorBackground: 'white',
      colorPrimary: '#DF1B41',
      colorPrimaryText: 'white',
      spacingGridRow: '15px'
    },
    rules: {
      '.Label': {
        marginBottom: '6px'
      },
      '.Tab, .Input, .Block': {
        boxShadow: '0px 3px 10px rgba(18, 42, 66, 0.08)',
        padding: '12px'
      }
    }
  };


card.mount('#card-element');
