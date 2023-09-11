<html>
<style>
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 100px auto;
    background-color: #555555;
}

form {
    display: inline-block;
    padding: 20px;
    border: 1px solid #ccc;
    background-color: #f9f9f9;
    border-radius: 10px;
    margin: 250px 400px;
}

input[type="text"],
select {
    padding: 10px;
    margin: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 150px;
}

select {
    width: 50px;
}

input[type="submit"] {
    padding: 10px 20px;
    background-color: #4caf50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #45a049;
}
</style>

<body>
    <form action="calc.php" method="post">
        <input type="text" name="n1" placeholder="Enter a Number" />
        <select name="op">
            <option value="add">+</option>
            <option value="sub">-</option>
            <option value="mul">x</option>
            <option value="div">/</option>
        </select>
        <input type="text" name="n2" placeholder="Enter a Number" />
        <input type="submit" value="CALC">
    </form>
</body>

</html>