window.addEventListener("DOMContentLoaded", () => {
    const savedNotes = localStorage.getItem("focusmate_notes");
    if (savedNotes) {
        document.getElementById("notes").value = savedNotes;
    }
});

// Save notes
function saveNotes() {
    const text = document.getElementById("notes").value;
    localStorage.setItem("focusmate_notes", text);

    const status = document.getElementById("noteStatus");
    status.innerText = "✅ Notes saved successfully";
    status.style.color = "green";
}