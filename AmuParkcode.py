import pymysql
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import PhotoImage
from PIL import ImageTk, Image  

try:
    db = pymysql.connect(host='localhost', user='root', password='root1234')
except pymysql.Error as e:
    print(e)

mc = db.cursor()

try:
    mc.execute('create database Amusement')
except pymysql.Error:
    print()

mc.execute("use Amusement")
print('Amusement Park Ticket Booking System'.center(155))
alter_query = "ALTER TABLE booking MODIFY COLUMN ID INT AUTO_INCREMENT"
mc.execute(alter_query)
db.commit()

# GUI initialization
root = Tk()
root.title("Amusement Park Ticket Booking System")

# Define functions for GUI interactions
def show_main_menu():
    main_menu_frame.pack()
    customer_menu_frame.pack_forget()
    admin_menu_frame.pack_forget()

def show_customer_menu():
    customer_menu_frame.pack()
    main_menu_frame.pack_forget()
    admin_menu_frame.pack_forget()

def show_admin_menu():
    admin_menu_frame.pack()
    main_menu_frame.pack_forget()
    customer_menu_frame.pack_forget()

def customer_login():
    show_customer_menu()

def admin_login():
    admin_password = admin_password_entry.get()
    if admin_password == "1234":
        show_admin_menu()
    else:
        messagebox.showerror("Error", "Wrong password")
def show_ride_information():
    # Implement ride information here
    ride_info = """
    AMUSEMENT PARK RIDES
    R1 - Ferris wheel (Price: 100 Rs)
    R2 - Carousel (Price: 100 Rs)
    R3 - Roller Coaster (Price: 100 Rs)
    R4 - Bumpy cars (Price: 100 Rs)
    R5 - Horror house (Price: 100 Rs)
    R6 - Sky Rocket (Price: 100 Rs)
    R7 - Mechanical Rodeo (Price: 100 Rs)
    R8 - Cup and saucer (Price: 100 Rs)
    R9 - Bungee (Price: 100 Rs)
    R10 - Kid's Room (Price: 100 Rs)
    """
    messagebox.showinfo("Ride Information", ride_info)


def book_tickets():
    # Hide the customer menu frame
    customer_menu_frame.pack_forget()

    # Create a new frame for input fields
    book_tickets_frame = Frame(root)
    Label(book_tickets_frame, text="Enter Customer Information", font=("Arial", 14)).pack(pady=20)

    # Create Entry widgets for user input
    name_entry = Entry(book_tickets_frame)
    age_entry = Entry(book_tickets_frame)
    height_entry = Entry(book_tickets_frame)
    phone_entry = Entry(book_tickets_frame)
    mail_entry = Entry(book_tickets_frame)
    day_entry = Entry(book_tickets_frame)

    Label(book_tickets_frame, text="Name:").pack()
    name_entry.pack()
    Label(book_tickets_frame, text="Age (years):").pack()
    age_entry.pack()
    Label(book_tickets_frame, text="Height (cm):").pack()
    height_entry.pack()
    Label(book_tickets_frame, text="Phone:").pack()
    phone_entry.pack()
    Label(book_tickets_frame, text="E-mail:").pack()
    mail_entry.pack()
    Label(book_tickets_frame, text="Day for booking:").pack()
    day_entry.pack()

    # Create Entry widgets for ride selections
    ride_t1_entry = Entry(book_tickets_frame)
    ride_t2_entry = Entry(book_tickets_frame)
    ride_t3_entry = Entry(book_tickets_frame)
    ride_t4_entry = Entry(book_tickets_frame)
    ride_t5_entry = Entry(book_tickets_frame)
    ride_t6_entry = Entry(book_tickets_frame)
    ride_t7_entry = Entry(book_tickets_frame)
    ride_t8_entry = Entry(book_tickets_frame)

    Label(book_tickets_frame, text="Ride T1:").pack()
    ride_t1_entry.pack()
    Label(book_tickets_frame, text="Ride T2:").pack()
    ride_t2_entry.pack()
    Label(book_tickets_frame, text="Ride T3:").pack()
    ride_t3_entry.pack()
    Label(book_tickets_frame, text="Ride T4:").pack()
    ride_t4_entry.pack()
    Label(book_tickets_frame, text="Ride T5:").pack()
    ride_t5_entry.pack()
    Label(book_tickets_frame, text="Ride T6:").pack()
    ride_t6_entry.pack()
    Label(book_tickets_frame, text="Ride T7:").pack()
    ride_t7_entry.pack()
    Label(book_tickets_frame, text="Ride T8:").pack()
    ride_t8_entry.pack()

    def submit_booking():
        customer_name = name_entry.get()
        customer_age = age_entry.get()
        customer_height = height_entry.get()
        customer_phone = phone_entry.get()
        customer_mail = mail_entry.get()
        customer_day = day_entry.get()

    # Collect ride information from the Entry widgets
        ride_t1 = ride_t1_entry.get()
        ride_t2 = ride_t2_entry.get()
        ride_t3 = ride_t3_entry.get()
        ride_t4 = ride_t4_entry.get()
        ride_t5 = ride_t5_entry.get()
        ride_t6 = ride_t6_entry.get()
        ride_t7 = ride_t7_entry.get()
        ride_t8 = ride_t8_entry.get()

    # Perform the database operations with the collected values
    # Insert the customer details into the 'booking' table
        customer_data = (customer_name, customer_age, customer_height, customer_phone, customer_mail, customer_day)
        insert_customer_query = 'INSERT INTO booking (Name, Age, Height, Phone, Mail, Day) VALUES (%s, %s, %s, %s, %s, %s)'
        mc.execute(insert_customer_query, customer_data)

    # Get the last inserted customer ID
        customer_id = mc.lastrowid

    # Insert the ride information into the 'timeslot' table
        ride_data = (customer_id, ride_t1, ride_t2, ride_t3, ride_t4, ride_t5, ride_t6, ride_t7, ride_t8)
        insert_ride_query = 'INSERT INTO timeslot (ID, T1, T2, T3, T4, T5, T6, T7, T8) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        mc.execute(insert_ride_query, ride_data)

        db.commit()

    # Remove the booking frame and show the customer menu frame
        book_tickets_frame.pack_forget()
        show_customer_menu()

    # Display a confirmation message
        mc.execute("SELECT LAST_INSERT_ID();")
        user_id = mc.fetchone()[0]
        confirmation_message = f"Booking confirmed!\nUser ID: {user_id}\nThank you for booking with us."
        messagebox.showinfo("Booking Confirmation", confirmation_message)


    Button(book_tickets_frame, text="Show Ride Information", command=show_ride_information).pack()
    # Pack the booking frame to display it
    book_tickets_frame.pack()
    
    Button(book_tickets_frame, text="Submit Booking", command=submit_booking).pack()
    tk.Button(edit_booking_frame, text="Back to Main Menu", command=return_to_main_menu).pack()
    # Pack the booking frame to display it
    book_tickets_frame.pack()

def check_booking():
    def show_booking_info():
        ui = user_id_entry.get()
        mc.execute('SELECT * FROM booking WHERE ID=%s', ui)
        r1 = mc.fetchall()
        mc.execute('SELECT * FROM timeslot WHERE ID=%s', ui)
        r2 = mc.fetchall()

        if r1 and r2:
            booking_info = f"Booking Details for User ID {ui}:\n"
            booking_info += "Customer Information:\n"
            for row in r1:
                booking_info += f"Name: {row[1]}\nAge: {row[2]}\nHeight: {row[3]}\nPhone: {row[4]}\nMail: {row[5]}\nDay: {row[6]}\n"
            booking_info += "\nRide Selections:\n"
            for row in r2:
                booking_info += f"T1: {row[1]}\nT2: {row[2]}\nT3: {row[3]}\nT4: {row[4]}\nT5: {row[5]}\nT6: {row[6]}\nT7: {row[7]}\nT8: {row[8]}\n"

            messagebox.showinfo("Booking Details", booking_info)
        else:
            messagebox.showerror("Error", f"Booking with User ID {ui} not found.")
    def return_to_main_menu():
        check_booking_frame.destroy()  # Destroy the check_booking_frame
        show_main_menu()

    # Add your code to retrieve and display booking information
    # Create a new frame for input
    check_booking_frame = Frame(root)
    Label(check_booking_frame, text="Enter User ID to Check Booking", font=("Arial", 14)).pack(pady=20)
    user_id_entry = Entry(check_booking_frame)
    user_id_entry.pack()
    Button(check_booking_frame, text="Check Booking", command=show_booking_info).pack()
    Button(check_booking_frame, text="Back to Main Menu", command=return_to_main_menu).pack()

    # Pack the frame to display it
    check_booking_frame.pack()


def edit_booking():
    def return_to_main_menu():
        edit_booking_frame.destroy()
        show_main_menu()

    def edit_user_info():
        ui = user_id_entry.get()
        mc.execute('select * from booking where id=%s', ui)
        user_data = mc.fetchone()
        if user_data:
            edit_user_info_window = tk.Toplevel(root)
            edit_user_info_window.title("Edit User Information")

            tk.Label(edit_user_info_window, text="Edit User Information", font=("Arial", 14)).pack(pady=20)
            tk.Label(edit_user_info_window, text="User ID: " + str(user_data[0])).pack()

            # Create and display the user information fields
            labels = []
            entries = []

            for i, field_name in enumerate(["Name", "Age", "Height", "Phone", "E-mail", "Day"]):
                label = tk.Label(edit_user_info_window, text=f"{field_name}: {user_data[i + 1]}")
                entry = tk.Entry(edit_user_info_window)
                entry.insert(0, user_data[i + 1])
                labels.append(label)
                entries.append(entry)
                label.pack()
                entry.pack()

            def submit_updated_user_info():
                updated_data = [entry.get() for entry in entries]

                for i, field_name in enumerate(["Name", "Age", "Height", "Phone", "Mail", "Day"]):
                    if updated_data[i]:
                        mc.execute(f'update booking set {field_name}=%s where id=%s', (updated_data[i], ui))

                db.commit()
                messagebox.showinfo("Success", "User information updated successfully!")
                edit_user_info_window.destroy()

            submit_button = tk.Button(edit_user_info_window, text="Submit Updated Info", command=submit_updated_user_info)
            submit_button.pack()

        else:
            messagebox.showerror("Invalid User ID", "User ID not found. Please enter a valid User ID.")
        

    def edit_ride_selections():
        ui = user_id_entry.get()
        mc.execute('select * from timeslot where id=%s', ui)
        ride_data = mc.fetchone()
        if ride_data:
            ride_selection_window = tk.Toplevel(root)
            ride_selection_window.title("Edit Ride Selections")

            tk.Label(ride_selection_window, text="Edit Ride Selections", font=("Arial", 14)).pack(pady=20)
            tk.Label(ride_selection_window, text="User ID: " + str(ride_data[0])).pack()

            # Create and display the ride selection fields
            labels = []
            entries = []

            for i in range(1, len(ride_data)):
                label = tk.Label(ride_selection_window, text=f"T{i} Ride:")
                entry = tk.Entry(ride_selection_window)
                entry.insert(0, ride_data[i])
                labels.append(label)
                entries.append(entry)
                label.pack()
                entry.pack()

            def submit_updated_ride_info():
                updated_data = [entry.get() for entry in entries]

                for i in range(len(updated_data)):
                    mc.execute(f'update timeslot set T{i+1}=%s where id=%s', (updated_data[i], ui))

                db.commit()
                messagebox.showinfo("Success", "Ride selections updated successfully!")
                ride_selection_window.destroy()

            submit_button = tk.Button(ride_selection_window, text="Submit Updated Ride Info", command=submit_updated_ride_info)
            submit_button.pack()

        else:
            messagebox.showerror("Invalid User ID", "User ID not found. Please enter a valid User ID.")

    edit_booking_frame = tk.Frame(root)
    tk.Button(edit_booking_frame, text="Back to Main Menu", command=return_to_main_menu).pack()
    tk.Label(edit_booking_frame, text="Edit Booking", font=("Arial", 14)).pack(pady=20)

    tk.Label(edit_booking_frame, text="Enter User ID:").pack()
    user_id_entry = tk.Entry(edit_booking_frame)
    user_id_entry.pack()

    tk.Button(edit_booking_frame, text="Edit User Information", command=edit_user_info).pack()
    tk.Button(edit_booking_frame, text="Edit Ride Selections", command=edit_ride_selections).pack()

    edit_booking_frame.pack()

def cancel_booking():
    def confirm_cancel():
        ui = user_id_entry.get()
        mc.execute('SELECT * FROM booking WHERE ID=%s', ui)
        current_booking = mc.fetchone()

        if current_booking:
            confirmation = messagebox.askquestion("Confirm Cancelation", "Do you want to cancel the booking with User ID {}?".format(ui))
            if confirmation == "yes":
                mc.execute('DELETE FROM booking WHERE ID=%s', ui)
                db.commit()
                mc.execute('DELETE FROM timeslot WHERE ID=%s', ui)
                db.commit()
                messagebox.showinfo("Booking Canceled", "Booking with User ID {} has been canceled.".format(ui))
        else:
            messagebox.showerror("Invalid User ID", "User ID not found. Please enter a valid User ID.")

    cancel_booking_frame = Toplevel(root)
    cancel_booking_frame.title("Cancel Booking")
    Label(cancel_booking_frame, text="Enter User ID:", font=("Arial", 12)).pack()
    user_id_entry = Entry(cancel_booking_frame)
    user_id_entry.pack()
    Button(cancel_booking_frame, text="Cancel Booking", command=confirm_cancel).pack()

    # Close the pop-up window when the user is done
    def close_window():
        cancel_booking_frame.destroy()
    Button(cancel_booking_frame, text="Close", command=close_window).pack()

# The main application window will remain open

def generate_bill():
    def calculate_bill():
        ui = user_id_entry.get()
        mc.execute('SELECT * FROM timeslot WHERE ID=%s', ui)
        current_timeslot = mc.fetchone()
        
        if current_timeslot:
            s = 0
            ride_prices = {
                'R1': 100, 'R2': 100, 'R3': 100, 'R4': 100,
                'R5': 100, 'R6': 100, 'R7': 100, 'R8': 100,
                'R9': 100, 'R10': 100
            }

            for i in range(1, 9):
                ride_code = current_timeslot[i]
                s += ride_prices.get(ride_code, 0)

            messagebox.showinfo("Total Bill", "Your total bill is {} Rs.".format(s))
        else:
            messagebox.showerror("Invalid User ID", "User ID not found. Please enter a valid User ID.")

    generate_bill_frame = Toplevel(root)
    generate_bill_frame.title("Generate Bill")
    Label(generate_bill_frame, text="Enter User ID:", font=("Arial", 12)).pack()
    user_id_entry = Entry(generate_bill_frame)
    user_id_entry.pack()
    Button(generate_bill_frame, text="Calculate Bill", command=calculate_bill).pack()

    # Close the pop-up window when you're done
    def close_window():
        generate_bill_frame.destroy()
    Button(generate_bill_frame, text="Close", command=close_window).pack()

# The main application window will remain open


def check_scheduled_bookings():
    def display_scheduled_bookings():
        mc.execute('SELECT * FROM booking')
        scheduled_bookings = mc.fetchall()
        if scheduled_bookings:
            scheduled_bookings_frame = Toplevel(root)
            scheduled_bookings_frame.title("Scheduled Bookings")
            Label(scheduled_bookings_frame, text="Scheduled Bookings", font=("Arial", 14)).pack(pady=20)

            scheduled_bookings_text = Text(scheduled_bookings_frame, width=60, height=20)
            scheduled_bookings_text.pack()

            for booking in scheduled_bookings:
                scheduled_bookings_text.insert(END, f"User ID: {booking[0]}\n")
                scheduled_bookings_text.insert(END, f"Name: {booking[1]}\n")
                scheduled_bookings_text.insert(END, f"Age: {booking[2]}\n")
                scheduled_bookings_text.insert(END, f"Height: {booking[3]}\n")
                scheduled_bookings_text.insert(END, f"Phone: {booking[4]}\n")
                scheduled_bookings_text.insert(END, f"Mail: {booking[5]}\n")
                scheduled_bookings_text.insert(END, f"Day: {booking[6]}\n")
                scheduled_bookings_text.insert(END, "\n")

            scheduled_bookings_text.config(state=DISABLED)
        else:
            messagebox.showinfo("No Scheduled Bookings", "There are no scheduled bookings.")

    scheduled_bookings_frame = Toplevel(root)
    scheduled_bookings_frame.title("Scheduled Bookings")
    Label(scheduled_bookings_frame, text="Check Scheduled Bookings", font=("Arial", 14)).pack(pady=20)
    Button(scheduled_bookings_frame, text="Display Scheduled Bookings", command=display_scheduled_bookings).pack()

# The main application window will remain open


def view_customer_details():
    def display_customer_details():
        ui = user_id_entry.get()
        mc.execute('SELECT * FROM booking WHERE ID=%s', ui)
        customer_details = mc.fetchall()
        if customer_details:
            customer_details_frame = Toplevel(root)
            customer_details_frame.title("Customer Details")
            Label(customer_details_frame, text="Customer Details", font=("Arial", 14)).pack(pady=20)

            customer_details_text = Text(customer_details_frame, width=60, height=20)
            customer_details_text.pack()

            for detail in customer_details:
                customer_details_text.insert(END, f"User ID: {detail[0]}\n")
                customer_details_text.insert(END, f"Name: {detail[1]}\n")
                customer_details_text.insert(END, f"Age: {detail[2]}\n")
                customer_details_text.insert(END, f"Height: {detail[3]}\n")
                customer_details_text.insert(END, f"Phone: {detail[4]}\n")
                customer_details_text.insert(END, f"Mail: {detail[5]}\n")
                customer_details_text.insert(END, f"Day: {detail[6]}\n")
                customer_details_text.insert(END, "\n")

            customer_details_text.config(state=DISABLED)
        else:
            messagebox.showerror("Error", "User ID not found!")

    view_customer_details_frame = Toplevel(root)
    view_customer_details_frame.title("View Customer Details")
    Label(view_customer_details_frame, text="View Customer Details", font=("Arial", 14)).pack(pady=20)

    user_id_label = Label(view_customer_details_frame, text="Enter User ID:")
    user_id_label.pack()
    user_id_entry = Entry(view_customer_details_frame)
    user_id_entry.pack()

    display_button = Button(view_customer_details_frame, text="Display Customer Details", command=display_customer_details)
    display_button.pack()

# The main application window will remain open


def clear_system():
    def clear_database():
        admin_password = admin_password_entry.get()
        if admin_password == "Summer123":  # Change to the desired password
            mc.execute("DELETE FROM booking")
            mc.execute("DELETE FROM timeslot")
            db.commit()
            messagebox.showinfo("Success", "System cleared successfully.")
        else:
            messagebox.showerror("Error", "Incorrect password!")

    clear_system_frame = Toplevel(root)
    clear_system_frame.title("Clear System")
    Label(clear_system_frame, text="Clear System", font=("Arial", 14)).pack(pady=20)

    password_label = Label(clear_system_frame, text="Enter Admin Password:")
    password_label.pack()
    admin_password_entry = Entry(clear_system_frame, show="*")
    admin_password_entry.pack()

    clear_button = Button(clear_system_frame, text="Clear System", command=clear_database)
    clear_button.pack()

# The main application window will remain open
# Create and display main menu frame
main_menu_frame = Frame(root)

main_menu_frame.pack()

Label(main_menu_frame, text="Amusement Park Ticket Booking System", font=("Arial", 16)).pack(pady=20)
Button(main_menu_frame, text="Customer Menu", command=customer_login).pack()
Label(main_menu_frame, text="Admin Menu (Password required)", font=("Arial", 12)).pack()
admin_password_entry = Entry(main_menu_frame, show="*")
admin_password_entry.pack()
Button(main_menu_frame, text="Admin Menu", command=admin_login).pack()

# Create and display customer menu frame
customer_menu_frame = Frame(root)
def return_to_main_menu():
    show_main_menu()
Button(customer_menu_frame, text="Back to Main Menu", command=return_to_main_menu).pack()
Label(customer_menu_frame, text="Customer Menu", font=("Arial", 14)).pack(pady=20)
Button(customer_menu_frame, text="Book Tickets", command=book_tickets).pack()
Button(customer_menu_frame, text="Check Booking", command=check_booking).pack()
Button(customer_menu_frame, text="Edit Booking", command=edit_booking).pack()
Button(customer_menu_frame, text="Cancel Booking", command=cancel_booking).pack()
Button(customer_menu_frame, text="Generate Bill", command=generate_bill).pack()

# Create and display admin menu frame
admin_menu_frame = Frame(root)
Button(admin_menu_frame, text="Back to Main Menu", command=return_to_main_menu).pack()
Label(admin_menu_frame, text="Admin Menu", font=("Arial", 14)).pack(pady=20)
Button(admin_menu_frame, text="Check Scheduled Bookings", command=check_scheduled_bookings).pack()
Button(admin_menu_frame, text="View Customer Details", command=view_customer_details).pack()
Button(admin_menu_frame, text="Edit Booking", command=edit_booking).pack()
Button(admin_menu_frame, text="Clear System", command=clear_system).pack()
root.mainloop()
