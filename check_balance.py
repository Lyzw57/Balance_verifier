def check_balance(balance_before: float, change_in_plus: float, change_in_minus: float, exchange_rate: float) -> float:
	"""Adjust opening balance by incoming and outgoing payments and returns updated balance.

	Args:
		balance_before (float): opening balance of bank account.
		change_in_plus (float): incoming payments.
		change_in_minus (float): outgoing payments.
		exchange_rate (float): exchange rate for currency.

	Returns:
		float: balance adjusted by incoming and outgoing payments.
	"""
	balance_after = balance_before + round((change_in_plus / exchange_rate),2) - round((change_in_minus / exchange_rate), 2)
	return balance_after
	
def get_user_input():
	"""Takes the floating point number from user.

	Returns:
		float: floating point number entered by user.
	"""
	while True:
		try:
			user_input = float(input())
			return user_input
		except ValueError:
			print("Blad, sprobuj ponownie!", end=" ")		

def show_result(balance_after: float):
	"""Prints bank balance after changes made by incoming and outgoing payments.

	Args:
		balance_after (float): balance changed by incoming and outgoing payments.
	"""
	print(f"Saldo po zmianach: {balance_after:,.2f}")
	
def init_calc():
	"""
	Handle script's logic.
	"""
	print("Podaj saldo poprzednie: ", end=" ")
	balance_before = get_user_input()
	print("Podaj zmiany na plus: ", end=" ")
	change_in_plus = get_user_input()
	print("Podaj zmiany na minus: ", end=" ")
	change_in_minus = get_user_input()
	print("Podaj kurs: ", end=" ")
	exchange_rate = get_user_input()
	balance_after = check_balance(balance_before, change_in_plus, change_in_minus, exchange_rate)
	show_result(balance_after)
	
if __name__ == "__main__":
	init_calc()
