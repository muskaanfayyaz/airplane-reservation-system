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
    fares = plane.get_fares()
    for cls, fare in fares.items():
        st.write(f"**{cls}:** Rs. {fare:,} 💵")

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
