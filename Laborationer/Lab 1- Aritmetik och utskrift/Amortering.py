def kostnad(P, r, a):
    k = P + (a + 1) * P * r / 2
    print(f"Den totala kostnaden efter {a} år är {k:.0f} kr.")

kostnad(50000, 0.03, 10)
# Den totala kostnaden efter 10 år är 58250 kr.
