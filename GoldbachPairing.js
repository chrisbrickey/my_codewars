function isPrime(number) {
    if (number == 1) { return false; }
    if (number <= 3) { return true; }
    if (number % 2 == 0 || number % 3 == 0) { return false; }
    var i = 5;
    while (i * i <= number) {
      if (number % i == 0 || number % (i + 2) == 0) {
        return false;
      }
      i = i + 6
    }

    return true;
}

function checkGoldbach(number) {
    if (number > 2 && number % 2 == 0) {
        var addend = 2;

        while(true) {
            var augend = number - addend;
            if (isPrime(addend) && isPrime(augend)) {
                return [addend, augend];
            }

            addend++;
            while (!isPrime(addend)) {
                addend++;
            }
        }
    }

    return [];
}
