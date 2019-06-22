// WIndowsConsoleApplication.cpp : This file contains the 'main' function. Program execution begins and ends there.
#include "pch.h"
#include <iostream>
#include <string>
#include "Header.h"
#include<vector>

class Person {
public: 
	std::string person_name;
	std::string email_id;
	std::string phone_number;
	std::string choice_of_car;

	void initialize_person(std::string person_name, std::string email_id, std::string phone_number, std::string choice_of_car) {
		person_name = person_name;
		email_id = email_id;
		phone_number = phone_number;
		choice_of_car = choice_of_car;
	}

	void print_person_details() {
		std::cout << person_name << std::endl;
		std::cout << email_id << std::endl;
		std::cout << phone_number << std::endl;
		std::cout << choice_of_car << std::endl;
	}

};

void update_field(std::string field_name, Person person) {
	
	if (field_name == "person_name") {
		std::string updated_person_name;
		std::cout << "Enter the updated value of the field";
		std::cin >> updated_person_name;
		person.person_name = updated_person_name;
	}
	else if (field_name == "email_id") {
		std::string updated_email;
		std::cout << "Enter the updated email_ id";
		std::cin >> updated_email;
		person.email_id = updated_email;
	}
	else if (field_name == "phone_number") {
		std::string updated_number;
		std::cout << " Enter the updatd phone numver";
		std::cin >> updated_number;
		person.phone_number = updated_number;
	}
	else if (field_name == "choice_of_car") {
		std::string updated_car;
		std::cout << "Enter the updated car of choice";
		std::cin >> updated_car;
		person.choice_of_car = updated_car;
	}
}

Person create_new_customer_account(Person person) {
	std::string name, email, number, car;
	std::cout << "Enter the name of the person ";
	std::cin >> name;
	person.person_name = name;
	std::cout << "Enter the email id ";
	std::cin >> email;
	person.email_id = email;
	std::cout << "Enter the phone Number";
	std::cin >> number;
	person.phone_number = number;
	std::cout << "Enter chouice of car";
	std::cin >> car;
	person.choice_of_car = car;
	return person;
}

Person update_user_wrt_field_name(std::string field_name, Person person) {
	if (field_name == "person_name") {
		std::string person_name;
		std::cout << "Ente the updated person name";
		std::cin >> person_name;
		person.person_name = person_name;
		return person;
	}


}

void update_existing_user(std::vector<Person> users) {
	int i;
	std::string person_name, field_name;
	Person updated_person;
	std::cout << "Enter the name of the person whse details are to be updated";
	std::cin >> person_name;
	for (i = 0; i < users.size(); i++) {
		if (users[i].person_name == person_name) {
			std::cout << "Enter the field to be updated";
			std::cin >> field_name;
			updated_person = update_user_wrt_field_name(field_name, users[i]);
			users.at(i) = updated_person;
			//std::replace(users.begin(), users.end(), users[i], updated_person );
		}
	}
}


int display_main_options() {
	int choice;
	std::cout << "Select your choice" << std::endl;
	std::cout << "1.) Create new account" << std::endl;
	std::cout << "2.) Update information of existing user" << std::endl;
	std::cout << "3.) For transactions" << std::endl;
	std::cout << "4.) Check details of existing user" << std::endl;
	std::cout << "5.) Remove existing account" <<std::endl;
	std::cout << "6.) View Customers List" <<std::endl;
	std::cout << "7.) Exit" << std::endl;
	std::cin >> choice;
	return choice;
}

void display_user_information(std::vector <Person> users) {
	int i;
	std::string person_name;
	std::cout << "Enter the name of the person ";
	std::cin >> person_name;
	for (i = 0; i < users.size(); i++) {
		if (users[i].person_name == person_name) {
			std::cout << "Person Name: " << users[i].person_name;
			std::cout << "Email Id: " << users[i].email_id;
			std::cout << "Phone Number " << users[i].phone_number;
			std::cout << "Car Of Choice " << users[i].choice_of_car;
		}
	}
}

void view_users_list(std::vector <Person> users) {
	int i;
	for (i = 0; i < users.size(); i++) {
		std::cout << users[i].person_name<< std::endl;
	}
}

std::vector <Person> remove_element(std::vector <Person> users, Person person) {
	int i;
	std::vector <Person> temp_vector;
	for (i = 0; i < users.size(); i++) {
		if (users[i].person_name == person.person_name) {
			i++;
		}
		else {
			temp_vector.push_back(users[i]);
		}
	}

	return temp_vector;
}

void delete_user(std::vector <Person> users) {
	int i;
	std::vector <Person> updated_users;
	std::string person_name;

	std::cout << "Enter the name of the person to be deleted";
	std::cin >> person_name;

	for (i = 0; i < users.size(); i++) {
		if (users[i].person_name == person_name) {
		updated_users = remove_element(users, users[i]);
		

		}
	}
}

void take_actions_wrt_choice(int user_choice_main_page, std::vector <Person> users) {
	int user_choice;
	if (user_choice_main_page == 1) {
		Person new_object;
		new_object = Person();
		new_object = create_new_customer_account(new_object);
		users.push_back(new_object);
	}

	else if (user_choice_main_page == 2) {
		if (users.size() == 0) {
			display_main_options();
		}
		else {
			update_existing_user(users);
		}
	}

	else if (user_choice_main_page == 4) {
		display_user_information(users);
	}

	else if (user_choice_main_page == 6) {
		view_users_list(users);
	}

	else if (user_choice_main_page == 7) {
		exit(0);
	}
	else if (user_choice_main_page == 5) {
		delete_user(users);
	}

	user_choice = display_main_options();
	take_actions_wrt_choice(user_choice, users);
}

int main() {
	std::vector< Person > users;
	Person person, new_object;
	int new_or_existing_data_set;
	int user_choice_main_page;

	user_choice_main_page = display_main_options();
	take_actions_wrt_choice(user_choice_main_page, users);
	

	/*std::cout << "the name is " << person.person_name;
	person.print_person_details();

	std::cout << "Enter choice";
	std::cout << "1.) Modify exisiting data set";
	std::cout << "2.) Create new data set";
	std::cin >> new_or_existing_data_set; */

	
	return 0;
}
