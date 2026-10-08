import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import math

def solve_projection():
    # 1. Inputs (Source [1, 2])
    tl = float(input("True Length (TL): "))
    theta_d = float(input("True angle with HP (θ): "))
    phi_d = float(input("True angle with VP (φ): "))
    h_a = float(input("Height of A above HP (a'): "))
    d_a = float(input("Distance of A in-front of VP (a): "))

    try:
        print("\n")

        # 1. Geometric Impossibility: Sum of true angles cannot exceed 90 degrees
        # In orthographic projection, θ + φ must be <= 90° for a single line.
        if (theta_d + phi_d) > 90:
            print("INSOLVABLE")
            print("In orthographic projection, θ + φ must be <= 90° for a single line.")
            return

        # 2. Angle Range Validation: True angles must be between 0 and 90 degrees
        if not (0 <= theta_d <= 90) or not (0 <= phi_d <= 90):
            print("INSOLVABLE")
            print("Angle Range Validation: True angles must be between 0 and 90 degrees")
            return

        # 3. Length Constraint: True Length must be a positive value
        if tl <= 0:
            print("INSOLVABLE")
            print("Length Constraint: True Length must be a positive value")
            return

        # 4. Calculation Check: Ensure the projection is mathematically valid
        # If the trigonometry results in invalid values, it is insolvable.
        try:
            # Converting to radians for calculation
            theta_r = math.radians(theta_d)
            phi_r = math.radians(phi_d)
            
            # Apparent lengths derived from TL (Source [4])
            # If TL is too short to reach the next coordinate locus, it's insolvable.
            al_fv = tl * math.cos(phi_r)
            al_tv = tl * math.cos(theta_r)
            
        except (ValueError, ZeroDivisionError):
            print("INSOLVABLE")
            print("The trigonometry results in invalid values.")
            return

        print("Inputs validated. Proceeding with projection...")
        # ... plotting logic would follow here ...

    except ValueError:
        # Triggered if user enters non-numeric text
        print("INSOLVABLE")
        print("Please enter valid numerical values for all inputs.")
        return

    # Plotting 
    # 2. Calculations 
    theta, phi = math.radians(theta_d), math.radians(phi_d)
    
    # TV and FV radii for construction
    tv_radius = tl * math.cos(theta) 
    fv_radius = tl * math.cos(phi)
    
    h_b = h_a + tl * math.sin(theta)
    d_b = d_a + tl * math.sin(phi)
    
    # Apparent Angles and Distance Between End Projectors (DEP)
    dep = math.sqrt(fv_radius**2 - (h_b - h_a)**2)
    alpha_d = math.degrees(math.atan2(h_b - h_a, dep))
    beta_d = math.degrees(math.atan2(d_b - d_a, dep))

    fig, ax = plt.subplots(figsize=(14, 11))
    ax.axhline(0, color='black', linewidth=2) # XY Line
    ax.text(-30, 5, "X", fontweight='bold'); ax.text(dep + 100, 5, "Y", fontweight='bold')

    # 3. Draw Locus Lines (Source [3, 4])
    ax.hlines([h_a, h_b], -20, dep + 90, colors='gray', linestyles='--', alpha=0.5)
    ax.hlines([-d_a, -d_b], -20, dep + 90, colors='gray', linestyles='--', alpha=0.5)
    ax.text(dep + 95, h_b, "Locus of b'"); ax.text(dep + 95, -d_b, "Locus of b")

    # 4. Angle Arcs and Numerical Values (Source [2, 3])
    # Notation: TI = True Inclination, AI = Apparent Inclination
    arc_rad = tl * 0.3 
    
    # Front View Angles: θ (True - Orange) and α (Apparent - Red)
    ax.add_patch(Arc((0, h_a), arc_rad, arc_rad, theta1=0, theta2=theta_d, color='orange', lw=2))
    ax.text(arc_rad/1.4 * math.cos(theta/2), h_a + arc_rad/1.4 * math.sin(theta/2), 
            f"$\\theta = {theta_d:.1f}^\\circ$", color='orange', fontweight='bold', fontsize=12)
    
    ax.add_patch(Arc((0, h_a), arc_rad*1.5, arc_rad*1.5, theta1=0, theta2=alpha_d, color='red', lw=2))
    ax.text(arc_rad*1.2 * math.cos(math.radians(alpha_d/2)), h_a + arc_rad*1.2 * math.sin(math.radians(alpha_d/2)), 
            f"$\\alpha = {alpha_d:.1f}^\\circ$", color='red', fontweight='bold', fontsize=12)

    # Top View Angles: φ (True - Orange) and β (Apparent - Blue)
    ax.add_patch(Arc((0, -d_a), arc_rad, arc_rad, theta1=-phi_d, theta2=0, color='orange', lw=2))
    ax.text(arc_rad/1.4 * math.cos(phi/2), -d_a - arc_rad/1.4 * math.sin(phi/2), 
            f"$\\phi = {phi_d:.1f}^\\circ$", color='orange', fontweight='bold', fontsize=12)
    
    ax.add_patch(Arc((0, -d_a), arc_rad*1.5, arc_rad*1.5, theta1=-beta_d, theta2=0, color='blue', lw=2))
    ax.text(arc_rad*1.2 * math.cos(math.radians(-beta_d/2)), -d_a + arc_rad*1.2 * math.sin(math.radians(-beta_d/2)), 
            f"$\\beta = {beta_d:.1f}^\\circ$", color='blue', fontweight='bold', fontsize=12)

    # 5. Draw True Length Positions (Source [2])
    ax.plot([0, tv_radius], [h_a, h_b], color='orange', marker='s', label=f"TL ({tl}) (a'B')")
    ax.text(tv_radius, h_b + 2, "B'")
    ax.plot([0, fv_radius], [-d_a, -d_b], color='orange', marker='s', label=f"TL ({tl}) (aB)")
    ax.text(fv_radius, -d_b - 10, "B")

    # 6. Construction Path (Source [3])
    # Path to b': B -> b'1 -> b'
    ax.vlines(fv_radius, -d_b, h_a, colors='green', linestyles=':') 
    ax.text(fv_radius, h_a + 2, "b'1")
    ax.add_patch(Arc((0, h_a), 2*fv_radius, 2*fv_radius, theta1=0, theta2=alpha_d, color='red', ls='--'))
    
    # Path to b: B' -> b1 -> b
    ax.vlines(tv_radius, h_b, -d_a, colors='green', linestyles=':') 
    ax.text(tv_radius, -d_a - 10, "b1")
    ax.add_patch(Arc((0, -d_a), 2*tv_radius, 2*tv_radius, theta1=-beta_d, theta2=0, color='blue', ls='--'))

    # 7. Final Projections (Source [3])
    ax.plot([0, dep], [h_a, h_b], 'r-o', linewidth=3, label=f"Front View (a'b') [AL={fv_radius:.1f}]")
    ax.text(-15, h_a + 2, "a'"); ax.text(dep, h_b + 2, "b'")
    
    ax.plot([0, dep], [-d_a, -d_b], 'b-o', linewidth=3, label=f"Top View (ab) [AL={tv_radius:.1f}]")
    ax.text(-15, -d_a - 12, "a"); ax.text(dep, -d_b - 12, "b")
    
    ax.vlines(0, -d_a, h_a, colors='black', linewidth=1.2); ax.vlines(dep, -d_b, h_b, colors='brown', linewidth=1.2)

    ax.set_title("Skew Line Projection: Rotation Method with Angle Values")
    ax.legend(loc='upper left'); plt.axis('equal'); plt.grid(True, alpha=0.2); plt.show()

    # 2. Calculations (Not in sources - standard geometric projection formulas)
    # Convert degrees to radians for math functions
    theta = math.radians(theta_d)
    phi = math.radians(phi_d)

    # Calculate lengths of projections
    tv_len = tl * math.cos(theta)  # Top View Length (Plan)
    fv_len = tl * math.cos(phi)    # Front View Length (Elevation)

    # Calculate apparent angles (alpha and beta)
    alpha = math.degrees(math.atan(math.tan(theta) / math.cos(phi)))
    beta = math.degrees(math.atan(math.tan(phi) / math.cos(theta)))

    # Calculate coordinates for point B
    h_b = h_a + (tl * math.sin(theta))
    d_b = d_a + (tl * math.sin(phi))

    # Calculate Distance Between End Projectors (DEP)
    dep = tv_len * math.cos(math.radians(beta))

    # 3. Output - Displaying all 12 values
    print("\n--- Projection Results ---")
    print(f"1.  True Length (TL): {tl}")
    print(f"2.  True angle with HP (θ): {theta_d}°")
    print(f"3.  True angle with VP (φ): {phi_d}°")
    print(f"4.  Height of A above HP (a'): {h_a}")
    print(f"5.  Distance of A in-front of VP (a): {d_a}")
    print(f"6.  Front View Length (FV): {round(fv_len, 2)}")
    print(f"7.  Top View Length (TV): {round(tv_len, 2)}")
    print(f"8.  Apparent angle with HP (α): {round(alpha, 2)}°")
    print(f"9.  Apparent angle with VP (β): {round(beta, 2)}°")
    print(f"10. Height of B above HP (b'): {round(h_b, 2)}")
    print(f"11. Distance of B in-front of VP (b): {round(d_b, 2)}")
    print(f"12. Distance Between End Projectors (DEP): {round(dep, 2)}")
solve_projection()
