function addTask() {
    let input = document.getElementById("taskInput");
    let taskText = input.value.trim();
    if (taskText === "") return;
    let listItem = document.createElement("li");
    listItem.className = "list-group-item d-flex justify-content-between align-items-center pending";
    listItem.innerHTML = `${taskText} <span>
        <button class='btn btn-success btn-sm' onclick='markTask(this)'>✔</button>
        <button class='btn btn-danger btn-sm' onclick='deleteTask(this)'>✖</button>
    </span>`;
    document.getElementById("taskList").appendChild(listItem);
    input.value = "";
}

function markTask(button) {
    let listItem = button.parentElement.parentElement;
    listItem.classList.toggle("completed");
    listItem.classList.toggle("pending");
}

function deleteTask(button) {
    let listItem = button.parentElement.parentElement;
    listItem.remove();
}

function deleteAll() {
    document.getElementById("taskList").innerHTML = "";
}