import turtle
def ana():
    print("╔══════════════════════╗")
    print("║     ŞEKİL ÇİZDİRME   ║")
    print("║        0-ÇEMBER      ║")
    print("║        3-ÜÇGEN       ║")
    print("║        4-DÖRTGEN     ║")
    print("║        5-BEŞGEN      ║")
    print("║        6-ALTIGEN     ║")
    print("║ ...DİĞERLERİ....     ║")
    print("║    /\       ____     ║")
    print("║   /  \     |    |    ║")
    print("║  /____\    |____|    ║")
    print("║    ____              ║")
    print("║   /    \     /\      ║")
    print("║  /      \   /  \     ║")
    print("║  \      /   \  /     ║")
    print("║   \____/     \/      ║")
    print("║                      ║")
    print("║                      ║")
    print("╚══════════════════════╝")
    secim=int(input(" KENAR SAYISI GİR"))
    if secim==0:
        t = turtle.Turtle()
        t.circle(100) 
    else:
        for x in range(secim):
            turtle.forward(100)
            turtle.right(360/secim)

