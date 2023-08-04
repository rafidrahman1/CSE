package com.example.localtpmg.service;

import com.example.localtpmg.entity.StudentEntity;
import com.example.localtpmg.models.StudentModel;

import java.util.List;

public interface StudentService {
    StudentEntity findStudentById(Long id);
    StudentEntity createStudent(StudentModel studentModel);
    List<StudentEntity> getStudentList();

}
