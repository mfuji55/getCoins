function change() {
    var dollars = .06;
	var dollarCoins = 0;
	var quarters = 0;
	var nickels = 0;
	var dimes = 0;
	var cents = 0;
	var remainder = 0;
	var pennies = 0;
	
    //your code here 
    console.log("hello");
	
	while (dollars > .01) {
		if (dollars / 1) {
			dollarCoins++;
			remainder = dollars % 1;
		}
		
		else if (remainder / .25) {
			quarters++;
			remainder = remainder % .25;
		}
		
		else if (remainder / .1) {
			dimes++;
			remainder = remainder % .1;
		}
		
		else if (remainder / .05) {
			nickles++;
			remainder = remainder % .05;
		}
		
		else if (remainder / .01) {
			pennies++;
			remainder = remainder % .01;
		}
		
		
			
	} 
	
	
}