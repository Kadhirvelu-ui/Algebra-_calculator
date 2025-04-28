# Ultimate Algebra Calculator with All Features
# Install required packages: pip install streamlit sympy

# MUST BE FIRST - Page configuration
import streamlit as st
st.set_page_config(
    page_title="Ultimate Algebra Calculator",
    layout="wide",
    page_icon="🧮",
    initial_sidebar_state="expanded"
)

# Import other libraries
import sympy as sp
from sympy import (
    sqrt, Rational, Eq, latex, symbols,
    solve, simplify, factor, expand, nsimplify,
    degree, diff, integrate, series
)

# Define mathematical symbols
x, y, z = symbols('x y z')

def quadratic_solver():
    st.header("🔍 Quadratic Equation Solver")
    st.markdown("Solve equations of form: **ax² + bx + c = 0**")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Enter coefficient a:", value=1.0, step=0.1)
    with col2:
        b = st.number_input("Enter coefficient b:", value=0.0, step=0.1)
    with col3:
        c = st.number_input("Enter coefficient c:", value=0.0, step=0.1)
    
    if st.button("Solve Quadratic Equation", type="primary"):
        if a == 0:
            st.error("Coefficient 'a' cannot be zero for quadratic equations!")
        else:
            # Solve equation
            eq = a*x**2 + b*x + c
            solutions = solve(eq, x)
            
            # Display results
            st.subheader("🎯 Solutions")
            st.latex(f"Equation: {latex(eq)} = 0")
            
            # Show discriminant
            discriminant = b**2 - 4*a*c
            st.write("**Discriminant Analysis:**")
            st.latex(f"D = b^2 - 4ac = {discriminant}")
            
            if discriminant > 0:
                st.write("Two distinct real roots")
            elif discriminant == 0:
                st.write("One real root (repeated)")
            else:
                st.write("Two complex roots")
            
            # Show solutions
            for i, sol in enumerate(solutions, 1):
                exact_sol = nsimplify(sol, tolerance=1e-9)
                st.latex(f"x_{i} = {latex(exact_sol)}")
                st.caption(f"Decimal approximation: ≈ {sol.evalf(5)}")
            
            # Show vertex form
            vertex_form = a*(x + b/(2*a))**2 + (c - b**2/(4*a))
            st.subheader("📊 Graphical Analysis")
            st.latex(f"Vertex form: {latex(vertex_form)}")
            st.write(f"Vertex at: ({-b/(2*a):.2f}, {c - b**2/(4*a):.2f})")

def expression_simplifier():
    st.header("✨ Expression Simplifier")
    expr_input = st.text_area(
        "Enter expression to simplify:",
        value="(x + 1)**2 - (x - 1)**2",
        height=70
    )
    
    if st.button("Simplify Expression", type="primary") and expr_input:
        try:
            expr = sp.sympify(expr_input)
            simplified = simplify(expr)
            
            st.subheader("Simplified Result")
            st.latex(f"{latex(expr)} \\Rightarrow {latex(simplified)}")
            
            # Show steps if complex
            if len(str(expr)) > 30:
                st.subheader("🔧 Simplification Steps")
                st.write("1. Expand all terms:")
                expanded = expand(expr)
                st.latex(f"{latex(expr)} = {latex(expanded)}")
                
                st.write("2. Combine like terms:")
                st.latex(f"{latex(expanded)} = {latex(simplified)}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

def polynomial_factorizer():
    st.header("🧩 Polynomial Factorizer")
    poly_input = st.text_area(
        "Enter polynomial to factor:",
        value="x**3 - 2*x**2 - 5*x + 6",
        height=70
    )
    
    if st.button("Factor Polynomial", type="primary") and poly_input:
        try:
            poly = sp.sympify(poly_input)
            factored = factor(poly)
            
            st.subheader("Factored Form")
            st.latex(f"{latex(poly)} = {latex(factored)}")
            
            # Show roots
            roots = solve(poly, x)
            if roots:
                st.subheader("🎯 Roots")
                for i, root in enumerate(roots, 1):
                    exact_root = nsimplify(root, tolerance=1e-9)
                    st.latex(f"x_{i} = {latex(exact_root)}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

def binomial_expander():
    st.header("➗ Binomial Expander")
    binomial_input = st.text_area(
        "Enter binomial to expand:",
        value="(x + 2)**5",
        height=70
    )
    
    if st.button("Expand Binomial", type="primary") and binomial_input:
        try:
            binomial = sp.sympify(binomial_input)
            expanded = expand(binomial)
            
            st.subheader("Expanded Form")
            st.latex(f"{latex(binomial)} = {latex(expanded)}")
            
            # Show binomial theorem steps
            if binomial.is_Pow and binomial.args[1].is_Integer:
                n = binomial.args[1]
                st.subheader("🔧 Binomial Theorem Steps")
                st.latex(f"(a + b)^n = \\sum_{{k=0}}^{n} \\binom{{n}}{{k}} a^{{n-k}}b^k")
                st.latex(f"Here a = {latex(binomial.args[0].args[0])}, b = {latex(binomial.args[0].args[1])}, n = {n}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

def main():
    st.title("🧮 Ultimate Algebra Calculator")
    st.markdown("""
    Solve, simplify, factor, and expand algebraic expressions with complete step-by-step solutions.
    """)
    
    # Operation selection
    operation = st.sidebar.selectbox(
        "Select Operation:",
        ["Quadratic Equation Solver", 
         "Expression Simplifier",
         "Polynomial Factorizer",
         "Binomial Expander"],
        index=0
    )
    
    st.divider()
    
    # Route to selected operation
    if operation == "Quadratic Equation Solver":
        quadratic_solver()
    elif operation == "Expression Simplifier":
        expression_simplifier()
    elif operation == "Polynomial Factorizer":
        polynomial_factorizer()
    elif operation == "Binomial Expander":
        binomial_expander()
    
    # Footer
    st.divider()
    st.caption("""
    **Notation Guide:**
    - Use * for multiplication (2*x)
    - Use ** or ^ for exponents (x**2 or x^2)
    - Use sqrt() for square roots
    - For fractions: (numerator)/(denominator)
    """)

if __name__ == "__main__":
    main()
