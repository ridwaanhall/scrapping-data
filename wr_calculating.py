MatchNow = float(input("Enter Match Now     : "))
WrNow    = float(input("Enter Win Rate Now  : "))
WrGoal   = float(input("Enter Win Rate Goal : "))

WinTotal    = MatchNow * (WrNow / 100)
WinLose     = MatchNow - WinTotal
RemainingWr = 100      - WrGoal
WrResult    = 100      / RemainingWr
Percent     = WinLose  * WrResult
Result      = Percent  - MatchNow
FinalMatch  = round(Result)
print(f"You need around {FinalMatch} wins without losing")
print(f"to achieve a {WrGoal}% win rate.")