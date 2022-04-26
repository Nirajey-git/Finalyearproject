  $(".dropify").dropify();
  const can_edit = $("#edit_form").attr("data-edit")
console.log('can-edit is ',can_edit)
  if (can_edit === "False") {
    $("#edit_form :input").prop("disabled", true);
  }
  $(".form-check").hide();
  const times = document.querySelectorAll(".timeinput");
  
  for (i of times) {
    i.type = "time";
  }

  $("form#formsetform input[type=text]").each(function(){
    $(this).prop( "readonly", true );
   });
   $("form#formsetform label.requiredField").each(function(){
    $(this).hide()
   });