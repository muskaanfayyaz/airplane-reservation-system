# main.py

import streamlit as st
from airplane import Airplane

# Set Streamlit page configuration
st.set_page_config(page_title="✈️ Airplane Reservation System", layout="wide", page_icon="✈️")

# Initialize session state for the airplane
if "airplane" not in st.session_state:
    st.session_state.airplane = Airplane()

plane = st.session_state.airplane

# Sidebar menu
st.sidebar.title("🛫 **Airplane Reservation**")
choice = st.sidebar.radio("**Select an option**", [
    "📅 Book Seats", "🛋️ View Seating Plan", "💰 View Fare(s)", "🔄 System Reset"
])

# Main Title
st.title("**✈️ Airplane Reservation System**")

if choice == "📅 Book Seats":
    st.subheader("🎟️ **Book Your Seat**")
    
    seat_class = st.selectbox("**Select Seat Class**", ["First Class", "Business Class", "Economy Class"], key="seat_class", index=0)
    seats_to_book = st.number_input("**Enter number of seats to book**", min_value=1, max_value=20, step=1, key="seats")

    # Add-ons for extra services
    st.markdown("### ✨ **Select Optional Add-ons**:")
    extra_legroom = st.checkbox("🌟 **Extra Legroom** (Rs. 500 per seat)", value=False)
    in_flight_meal = st.checkbox("🍽️ **In-Flight Meal** (Rs. 300 per seat)", value=False)
    priority_boarding = st.checkbox("⏳ **Priority Boarding** (Rs. 250 per seat)", value=False)

    # Calculate fare based on class and selected options
    base_fare = 0
    if seat_class == "First Class":
        base_fare = plane.get_fares()["First Class"]
    elif seat_class == "Business Class":
        base_fare = plane.get_fares()["Business Class"]
    else:
        base_fare = plane.get_fares()["Economy Class"]

    # Calculate additional costs based on selected add-ons
    extra_legroom_cost = 500 if extra_legroom else 0
    in_flight_meal_cost = 300 if in_flight_meal else 0
    priority_boarding_cost = 250 if priority_boarding else 0

    # Total cost calculation
    total_base_cost = base_fare * seats_to_book
    total_extra_cost = (extra_legroom_cost + in_flight_meal_cost + priority_boarding_cost) * seats_to_book
    total_cost = total_base_cost + total_extra_cost

    # Display calculated total cost
    st.markdown(f"### **Total Cost Breakdown**")
    st.write(f"🟩 **Base Fare for {seats_to_book} seat(s) in {seat_class}: Rs. {total_base_cost:,}")
    if extra_legroom:
        st.write(f"🌟 **Extra Legroom**: Rs. {extra_legroom_cost * seats_to_book:,}")
    if in_flight_meal:
        st.write(f"🍽️ **In-Flight Meal**: Rs. {in_flight_meal_cost * seats_to_book:,}")
    if priority_boarding:
        st.write(f"⏳ **Priority Boarding**: Rs. {priority_boarding_cost * seats_to_book:,}")
    st.markdown(f"**Total Amount**: Rs. {total_cost:,}")

    # Booking button
    booking_button = st.button("🔒 **Book Now**")

    if booking_button:
        if seat_class == "First Class":
            success = plane.book_first_class(seats_to_book)
        elif seat_class == "Business Class":
            success = plane.book_business_class(seats_to_book)
        else:
            success = plane.book_economy_class(seats_to_book)

        if success:
            st.success(f"🎉 **{seats_to_book} seat(s)** booked in **{seat_class}** successfully! ✅")
            st.success(f"💰 **Total Cost**: Rs. {total_cost:,}")
        else:
            st.error("🚫 **Booking Failed** — Not enough available seats.")

elif choice == "🛋️ View Seating Plan":
    st.subheader("🪑 **Current Seating Plan**")
    seats = plane.get_seats()

    for i, row in enumerate(seats):
        row_display = " ".join(["🟩" if seat == 0 else "🟥" for seat in row])
        st.markdown(f"**Row {i+1:02d}:** {row_display}")

elif choice == "💰 View Fare(s)":
    st.subheader("💸 **Fare Details**")
    
    # Enhanced Fare Breakdown
    fares = plane.get_fares()

    st.markdown("### ✨ **Class-wise Fare Breakdown**:")
    for cls, fare in fares.items():
        if cls == "First Class":
            st.markdown(f"**🌟 First Class:** Rs. {fare:,} 💎 - Experience the height of luxury with extra legroom, personalized service, and priority boarding.")
        elif cls == "Business Class":
            st.markdown(f"**💼 Business Class:** Rs. {fare:,} 💼 - Enjoy spacious seating, quick aisle access, and premium food & beverages.")
        else:
            st.markdown(f"**🌍 Economy Class:** Rs. {fare:,} 🌍 - Affordable comfort with standard amenities and great service.")

    # Option for add-ons
    st.markdown("""
    **Optional Add-ons**:
    - **Extra Legroom:** Rs. 500
    - **In-Flight Meal Upgrade:** Rs. 300
    - **Priority Boarding:** Rs. 250

    **Note**: Add-ons can be selected during the booking process.  
    """)

    st.markdown("___")
    st.markdown("💵 **Total Cost**: The final price will depend on the seat selection, add-ons, and any applicable discounts.")

elif choice == "🔄 System Reset":
    reset_button = st.button("🔄 **Reset All Seats**")
    if reset_button:
        plane.reset_system()
        st.success("🌟 **System Reset Successful** — All seats are now available! 🟩")

# Add footer
st.markdown(
    """
    ---
    🛫 **Thank you for using the Airplane Reservation System** ✈️.  
    **Developed with ❤️ by MUSKAAN**
    """
)
