import streamlit as st
import pandas as pd


# Main function
def main():
  st.title('Grade Tracker')

  st.subheader('Student Information')
  full_name = st.text_input('Full Name')
  symbol_number = st.text_input('Symbol Number')

  st.subheader('Grade Entry')

  # Semester selection
  semester_options = {
      '1st Sem': 1,
      '2nd Sem': 2,
      '3rd Sem': 3,
      '4th Sem': 4,
      '5th Sem': 5,
      '6th Sem': 6,
  }  # Semester options
  selected_semester = st.selectbox('Select Semester',
                                   list(semester_options.keys()))

  # Define subjects for each semester
  subjects = {
      1: [
          'Introduction to Information Technology', 'C Programming',
          'Digital Logic', 'Mathematics', 'Physics'
      ],
      2: [
          'Discrete Mathematics', 'Object-Oriented Programming',
          'Microprocessor', 'Mathematics II', 'Statistics I'
      ],
      3: [
          'Data Structures and Algorithms', 'Numerical Methods',
          'Computer Architecture', 'Computer Graphics', 'Statistics II'
      ],
      4: [
          'Database Management System', 'Operating Systems',
          'Computer Network', 'Artificial Intelligence',
          'Theory of Computation'
      ],
      5: [
          'Cryptography', 'Design and Analysis of Algorithms',
          'System Analysis and Design', 'Simulation and Modeling',
          'Web Technology'
      ],
      6: [
          'Software Engineering', 'Compiler Design and Constructin',
          'E-Governance', 'Net centric computing', 'Technical Writing'
      ]
  }

  # Input box for entering marks for corresponding subjects
  selected_subjects = subjects[semester_options[selected_semester]]
  marks = {}
  for subject in selected_subjects:
    marks[subject] = st.number_input(f'Enter Marks for {subject}',
                                     min_value=0,
                                     max_value=100,
                                     step=1,
                                     value=0)

  # Calculate total marks and percentage
  total_marks = sum(marks.values())
  total_subjects = len(selected_subjects)
  percentage = (total_marks / (total_subjects * 100)) * 100

  # Calculate GPA and Grade
  has_failed = any(mark < 40 for mark in marks.values())
  if has_failed:
    gpa = 0.0
    grade = 'F (Failed)'
  else:
    gpa = total_marks / (total_subjects * 25)
    if gpa >= 3.6:
      grade = 'A+'
    elif 3.2 <= gpa < 3.6:
      grade = 'A'
    elif 2.8 <= gpa < 3.2:
      grade = 'B+'
    elif 2.4 <= gpa < 2.8:
      grade = 'B'
    elif 2.0 <= gpa < 2.4:
      grade = 'C+'
    else:
      grade = 'D'

  # Save grade data to Excel file
  if st.button('Save Grades'):
    # Create a DataFrame with student information and grades
    data = {
        'Full Name': [full_name],
        'Symbol Number': [symbol_number],
        'Semester': [selected_semester],
        **marks, 'Total Marks': [total_marks],
        'Percentage': [percentage],
        'GPA': [gpa],
        'Grade': [grade]
    }
    df = pd.DataFrame(data)

    # Save DataFrame to Excel
    df.to_excel('grades.xlsx', index=False)
    st.success('Grades saved successfully!')


if __name__ == "__main__":
  main()
