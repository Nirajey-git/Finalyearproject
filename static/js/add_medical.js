FilePond.parse(document.body);
FilePond.registerPlugin(FilePondPluginImagePreview);

const pond = FilePond.create(document.querySelector("#filepondid"), {
  allowMultiple: true,
  instantUpload: false,
  allowProcess: false,
});

const myform = document.getElementById("formadd");

myform.addEventListener("submit", function (e) {
  e.preventDefault();
  var formdata = new FormData(myform);

  const pondFiles = pond.getFiles();

  formdata.append("csrfmiddlewaretoken", $("#formadd").attr("data-csrf"));

  for (var i = 0; i < pondFiles.length; i++) {
    formdata.append("files", pondFiles[i].file);
  }

  $.ajax({
    type: "post",
    url: $("#formadd").attr("data-url"),
    data: formdata,
    contentType: false,
    cache: false,
    processData: false,
    success: function (res) {
      if (res.added) {
          toastr.success('Medical History Added Successfully');
        myform.reset();
        pond.removeFiles();
      }
      else{
          toastr.error('Something Went Wrong');
      }
    },
  });
});