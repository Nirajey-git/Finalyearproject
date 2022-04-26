function rate_doctor(rating) {
    if (rating == 1) {
        $("#ratings").html(`
        <div class="star-review">
            <i onclick="rate_doctor(1)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(2)"  class="fa fa-star text-gray"></i>
            <i onclick="rate_doctor(3)" class="fa fa-star text-gray"></i>
            <i onclick="rate_doctor(4)" class="fa fa-star text-gray"></i>
            <i onclick="rate_doctor(5)" class="fa fa-star text-gray"></i>
        </div>
        `)
        $('#rating-value').html(1);

    }
    if (rating == 2) {
        $("#ratings").html(`
        <div class="star-review">
            <i onclick="rate_doctor(1)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(2)"  class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(3)" class="fa fa-star text-gray"></i>
            <i onclick="rate_doctor(4)" class="fa fa-star text-gray"></i>
            <i onclick="rate_doctor(5)" class="fa fa-star text-gray"></i>
        </div>
        `)
        $('#rating-value').html(2);
    }
    if (rating == 3) {
        $("#ratings").html(`
        <div class="star-review">
            <i onclick="rate_doctor(1)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(2)"  class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(3)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(4)" class="fa fa-star text-gray"></i>
            <i onclick="rate_doctor(5)" class="fa fa-star text-gray"></i>
        </div>
        `)
        $('#rating-value').html(3);
    }
    if (rating == 4) {
        $("#ratings").html(`
        <div class="star-review">
            <i onclick="rate_doctor(1)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(2)"  class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(3)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(4)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(5)" class="fa fa-star text-gray"></i>
        </div>
        `)
        $('#rating-value').html(4);
    }
    if (rating == 5) {
        $("#ratings").html(`
        <div class="star-review">
            <i onclick="rate_doctor(1)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(2)"  class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(3)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(4)" class="fa fa-star text-orange"></i>
            <i onclick="rate_doctor(5)" class="fa fa-star text-orange"></i>
        </div>
        `)
        $('#rating-value').html(5);
    }



    $.ajax({
        type: "post",
        url: $("#info-media").attr("data-url"),
        data: {
            doc_id: $("#info-media").attr("data-id"),
            rate: rating,
            csrfmiddlewaretoken: $("#info-media").attr("data-csrf"),
        },
        success: function(res) {
            console.log(res)
            toastr.success('Added your rating');
            $("#h_myrating").hide()
            $("#h_totalrating").hide()

            $("#myrating").removeClass("d-none")
            $("#totalrating").removeClass("d-none")

            $("#myrating").html(`Your Rating : ${res.myrate}`)
            $("#totalrating").html(`Total Rating : ${res.avg_rating}`)


            if ($("#first_to_rate")) {
                $("#first_to_rate").hide()
            }
        }
    });
}