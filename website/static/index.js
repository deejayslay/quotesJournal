// convert delete note to an http post method
function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function viewNote(noteId) {
  fetch("/view-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  })
    .then((res) => {
      res.json();
    })
    .then((data) => console.log(data));
}
