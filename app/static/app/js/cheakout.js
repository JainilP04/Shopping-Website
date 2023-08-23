$(document).ready (function () {

    $('.payWithRazorpay').click(function (e) {
         e.preventDefault();

         $.ajax({
             method:"GET",
             url: "/proceed-to-pay",
             success:function(response){
                 //console.log(response);
                 var options = {
                    "key": "rzp_test_ywgUI17AHk81LU", // Enter the Key ID generated from the Dashboard
                    //"amount": response.totalcost, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                    "currency": "INR",
                    "name": "Acme Corp",
                    "description": "Test Transaction",
                    "image": "https://example.com/your_logo",
                    "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                    "callback_url": "https://eneqd3r9zrjok.x.pipedream.net/",
                    "prefill": {
                        "name": "Gaurav Kumar",
                        "email": "gaurav.kumar@example.com",
                        "contact": "9999999999"
                    },
                    "notes": {
                        "address": "Razorpay Corporate Office"
                    },
                    "theme": {
                        "color": "#3399cc"
                    }
                };
                var rzp1 = new Razorpay(options);
                rzp1.open();
            
             }
         });


    });     

});