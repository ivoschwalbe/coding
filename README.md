### Aufgabe 1: Dreieck $FKR$ (Korrigierte Fassung)

**Gegeben:** $\gamma = 37^\circ$; $f = \overline{RK} = 19,2\text{ cm}$; $r = \overline{FK} = 17,3\text{ cm}$.

**Analyse der Bezeichnungen:**
In der Trigonometrie liegt die Seite $f$ dem Winkel bei $F$ gegenüber, $k$ dem Winkel bei $K$ ($\alpha$) und $r$ dem Winkel bei $R$ ($\beta$). Laut Skizze liegt $\gamma$ bei Punkt $F$.

**1. Schritt: Berechnung von Winkel $\beta$ (bei Punkt $R$) mit dem Sinussatz**
Da wir ein vollständiges Paar haben ($f$ und $\gamma$) und die Seite $r$ gegeben ist, suchen wir den gegenüberliegenden Winkel $\beta$:


$$\frac{\sin(\beta)}{r} = \frac{\sin(\gamma)}{f} \implies \sin(\beta) = \frac{\sin(37^\circ) \cdot 17,3}{19,2}$$

$$\sin(\beta) \approx \frac{0,6018 \cdot 17,3}{19,2} \approx 0,5423$$

$$\beta = \arcsin(0,5423) \approx \mathbf{32,84^\circ}$$

**2. Schritt: Berechnung von Winkel $\alpha$ (bei Punkt $K$)**
Über die Innenwinkelsumme im Dreieck:


$$\alpha = 180^\circ - 37^\circ - 32,84^\circ = \mathbf{110,16^\circ}$$

**3. Schritt: Berechnung der fehlenden Seite $k$ ($\overline{FR}$)**
Wieder mit dem Sinussatz (oder Kosinussatz möglich):


$$\frac{k}{\sin(\alpha)} = \frac{f}{\sin(\gamma)} \implies k = \frac{19,2 \cdot \sin(110,16^\circ)}{\sin(37^\circ)}$$

$$k \approx \frac{19,2 \cdot 0,9387}{0,6018} \approx \mathbf{29,95\text{ cm}}$$

---

### Aufgabe 2: Dreieck $FKR$

**Gegeben:** $\alpha = 48^\circ$; $r = \overline{FK} = 41,6\text{ cm}$; $f = \overline{RK} = 15,8\text{ cm}$.

**1. Schritt: Seite $k$ ($\overline{FR}$) mit dem Kosinussatz**
Da der Winkel $\alpha$ (bei $K$) zwischen den Seiten $f$ und $r$ liegt (SWS), nutzen wir den Kosinussatz:


$$k^2 = f^2 + r^2 - 2 \cdot f \cdot r \cdot \cos(\alpha)$$

$$k^2 = 15,8^2 + 41,6^2 - 2 \cdot 15,8 \cdot 41,6 \cdot \cos(48^\circ) \approx 1100,3$$

$$k = \sqrt{1100,3} \approx \mathbf{33,17\text{ cm}}$$

**2. Schritt: Weitere Winkel und Fläche**

* **Winkel $\gamma$:** $\frac{\sin(\gamma)}{15,8} = \frac{\sin(48^\circ)}{33,17} \implies \gamma \approx \mathbf{20,7^\circ}$
* **Winkel $\beta$:** $180^\circ - 48^\circ - 20,7^\circ = \mathbf{111,3^\circ}$
* **Fläche $A$:** $A = \frac{1}{2} \cdot f \cdot r \cdot \sin(\alpha) = \frac{1}{2} \cdot 15,8 \cdot 41,6 \cdot \sin(48^\circ) \approx \mathbf{244,1\text{ cm}^2}$

---

### Aufgabe 3: Rechtwinkliges Dreieck $ABC$

**Gegeben:** $\gamma = 90^\circ$; $\alpha = 16^\circ$; Hypotenuse $c = \overline{AB} = 54,2\text{ cm}$.

In rechtwinkligen Dreiecken nutzen wir direkt Definitionen von $\sin, \cos, \tan$:

* **Winkel $\beta$:** $90^\circ - 16^\circ = \mathbf{74^\circ}$
* **Seite $a$ (Gegenkathete zu $\alpha$):** $a = c \cdot \sin(16^\circ) = 54,2 \cdot 0,2756 \approx \mathbf{14,94\text{ cm}}$
* **Seite $b$ (Ankathete zu $\alpha$):** $b = c \cdot \cos(16^\circ) = 54,2 \cdot 0,9613 \approx \mathbf{52,10\text{ cm}}$
* **Fläche $A$:** $A = \frac{a \cdot b}{2} = \frac{14,94 \cdot 52,10}{2} \approx \mathbf{389,19\text{ cm}^2}$

---

**Kritische Anmerkung:** In Aufgabe 1 war die vorherige Fehlermeldung korrekt: Mit $19,2\text{ cm}$ statt $9,2\text{ cm}$ ist das Dreieck nun konstruierbar. Achte darauf, dass bei der Anwendung des Sinussatzes der gesuchte Winkel immer der Seite gegenüberliegen muss, die du in die Rechnung einbeziehst.

Soll ich dir zeigen, wie man die Ergebnisse durch eine Skizze grob auf Plausibilität prüft?
