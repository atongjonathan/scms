function handleFileSelected(input) {
    const fileName = input.files.length ? input.files[0].name : 'No file selected';
    document.getElementById('selected-file-name').textContent = fileName;

    // If user selects a new file, ensure the clear checkbox is unchecked
    document.querySelector('input[name="clear_image"]').checked = false;
}

function clearImage() {
    // Clear the file input (reset the form field)
    const fileInput = document.getElementById('real-file-input');
    fileInput.value = ''; // this clears the file input

    // Mark the clear checkbox
    document.querySelector('input[name="clear_image"]').checked = true;

    // Clear the preview text
    document.getElementById('selected-file-name').textContent = 'Image removed';

    // Optional: hide the nord-input with image info, show the attach button
    document.getElementById('existing-image-section').style.display = 'none';
    document.getElementById('upload-new-image-section').style.display = 'block';
}
