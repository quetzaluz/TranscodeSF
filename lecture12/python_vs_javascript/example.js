// Note: "print" is not a Javascript built-in like the Python one.
// The equivalent is console.log("text to print").
function runExample() {
    clearConsole();

    function tryGuess(num, guess) {
        if (guess < num) {
            print(guess + " is too low!");
        } else if (guess > num) {
            print(guess + " is too high!");
        } else {
            print(guess + " is right.  You win!");
        }
    }

    // Guess randomly until you win
    var secretNumber = Math.ceil(Math.random() * 5);
    var guess = undefined;
    while (guess != secretNumber) {
        guess = Math.ceil(Math.random() * 5);
        tryGuess(secretNumber, guess);
    }


    function isPrime(x) {
        for (var num = 2; num < x; num++) {
            // If x divides num evenly, then x is a factor of num.
            if (x % num == 0)
                return false;
        }
        return true;
    }

    var testNumbers = [2, 6, 13, 8, 20];
    for (var idx = 0; idx < testNumbers.length; idx++) {
        var y = testNumbers[idx];
        print(y + " is prime? " + isPrime(y));
    }

    var some_array = [1, 2, 4];  // Python lists == Javascript arrays
    var some_dict = {};
    some_dict['key_string'] = true;
    some_dict[3] = some_array;
    print(some_dict[3][1] + " should be " + 2);
}



// Some extra helper functions to output print() calls to the HTML page.
function print(text) {
    // Send text to developer console.
    console.log(text);

    // For ease of debugging, add output text to the page itself as well.
    page_console = document.getElementById('console');
    line = document.createElement("p");
    line.innerHTML = text;
    page_console.appendChild(line);
}

function clearConsole() {
    page_console = document.getElementById('console');
    page_console.innerHTML = "";
}
