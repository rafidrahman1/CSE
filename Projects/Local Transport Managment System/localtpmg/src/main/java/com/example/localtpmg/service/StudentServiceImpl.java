package com.example.localtpmg.service;

import com.example.localtpmg.entity.StudentEntity;
import com.example.localtpmg.models.StudentModel;
import com.example.localtpmg.repository.StudentRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class StudentServiceImpl implements StudentService {

    private final StudentRepository studentRepository;
    @Override
    public StudentEntity findStudentById(Long id) {
        return null;
    }

    @Override
    public StudentEntity createStudent(StudentModel studentModel) {
        StudentEntity student = StudentEntity.builder()//no need to build constructor
                .name(studentModel.getName())
                .creditCompleted(studentModel.getCreditCompleted())
                .cgpa(studentModel.getCgpa())
                .build();

        StudentEntity savedStudent =  studentRepository.save(student);//elborated
        return savedStudent;
   }

    @Override
    public List<StudentEntity> getStudentList() {
        List<StudentEntity> studentEntityList = studentRepository.findAll();
        return studentEntityList;
    }


}
