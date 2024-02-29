<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Handle image uploads
    $target_dir = "uploads/";
    $image1 = $target_dir . basename($_FILES["image1"]["name"]);
    $image2 = $target_dir . basename($_FILES["image2"]["name"]);
    $image3 = $target_dir . basename($_FILES["image3"]["name"]);

    $uploadOk = 1;
    $imageFileType1 = strtolower(pathinfo($image1, PATHINFO_EXTENSION));
    $imageFileType2 = strtolower(pathinfo($image2, PATHINFO_EXTENSION));
    $imageFileType3 = strtolower(pathinfo($image3, PATHINFO_EXTENSION));

    // Check if image file is a actual image or fake image
    $check1 = getimagesize($_FILES["image1"]["tmp_name"]);
    $check2 = getimagesize($_FILES["image2"]["tmp_name"]);
    $check3 = getimagesize($_FILES["image3"]["tmp_name"]);

    if ($check1 === false  $check2 === false  $check3 === false) {
        echo "File is not an image.";
        $uploadOk = 0;
    }

    // Check file size
    if ($_FILES["image1"]["size"] > 5000000  $_FILES["image2"]["size"] > 5000000  $_FILES["image3"]["size"] > 5000000) { // Adjust this value according to your needs
        echo "Sorry, your file is too large.";
        $uploadOk = 0;
    }

    // Allow certain file formats
    $allowed_extensions = array("jpg", "jpeg", "png", "gif");
    if (!in_array($imageFileType1, $allowed_extensions)  !in_array($imageFileType2, $allowed_extensions)  !in_array($imageFileType3, $allowed_extensions)) {
        echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
        $uploadOk = 0;
    }

    // Check if $uploadOk is set to 0 by an error
    if ($uploadOk == 0) {
        echo "Sorry, your file was not uploaded.";
    } else {
        if (move_uploaded_file($_FILES["image1"]["tmp_name"], $image1) &&
            move_uploaded_file($_FILES["image2"]["tmp_name"], $image2) &&
            move_uploaded_file($_FILES["image3"]["tmp_name"], $image3)) {
            // Handle other form fields
            $location = $_POST["location"];
            $price = $_POST["price"];
            $quantity = $_POST["quantity"];
            $ready_for_purchase = $_POST["ready_for_purchase"];
            $purchase_timeframe = $_POST["purchase_timeframe"];
            $contact = $_POST["contact"];

            // Here you can do further processing like storing the data in a database, sending emails, etc.
            echo "Product uploaded successfully.";
        } else {
            echo "Sorry, there was an error uploading your file.";
        }
    }
}
?>