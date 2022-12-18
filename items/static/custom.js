alertify.set('notifier','position', 'top-center');

$('.addToOrderBtn').click(function (e) {
    e.preventDefault();

    var product_id = $('.item_id').val();
    var quantity = $('.qty-input').val();

    $.ajax({
        method: "POST",
        url: "/add_order",
        data: {
            'product_id' : product_id,
            'quantity' : quantity,
        },
        success: function (response) {
            alertify.success(response.status)
        }
        });
});



