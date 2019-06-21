// WIndowsConsoleApplication.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
#include "Header.h"

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

int main() {
	std::string name, email, number, car;
	Person person;

	std::cout << "Enter the name of the person ";
	std::cin >> name;
	person.person_name = name;
	std::cout << "Enter the email id "; 
	std::cin >> email;

	std::cout << "Enter the phone Number";
	std::cin >> number;

	std::cout << "Enter chouice of car";
	std::cin >> car;

	person.initialize_person(name, email, number, car);
	std::cout << "the name is " << person.person_name;
	person.print_person_details();
	return 0;
}