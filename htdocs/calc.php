<html>

<style>
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 100px auto;
    background-color: #555555;
}

.answer-container {
    text-align: center;
    padding: 20px;
    margin: 350px 400px;
}

.answer {
    font-size: 20px;
    font-weight: bold;
    font-family: Arial, sans-serif;
    color: #333;
    background-color: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
}
</style>

<body>

    <?php


    if (isset($_POST['n1']) && isset($_POST['n2']) && isset($_POST['op']))
        if ($_POST['op'] == "add")
            $ans = ($_POST['n1'] . ' + ' . $_POST['n2'] . ' = ' . ($_POST['n1'] + $_POST['n2']));
        elseif ($_POST['op'] == "sub")
            $ans = ($_POST['n1'] . ' - ' . $_POST['n2'] . ' = ' . ($_POST['n1'] - $_POST['n2']));
        elseif ($_POST['op'] == "mul")
            $ans = ($_POST['n1'] . ' x ' . $_POST['n2'] . ' = ' . ($_POST['n1'] * $_POST['n2']));
        elseif ($_POST['op'] == "div")
            if ($_POST['n2'] == 0)
                $ans = "Cannot divide by zero";
            else
                $ans = ($_POST['n1'] . ' / ' . $_POST['n2'] . ' = ' . ($_POST['n1'] / $_POST['n2']));
        else
            $ans = "Invalid operator";
    else
        $ans = "Invalid inputs";

    ?>

    <div class="answer-container">
        <p class="answer"><?php echo $ans; ?></p>
    </div>

</body>

</html>