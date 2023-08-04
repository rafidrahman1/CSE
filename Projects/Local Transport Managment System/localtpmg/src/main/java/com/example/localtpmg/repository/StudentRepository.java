package com.example.localtpmg.repository;

import com.example.localtpmg.entity.StudentEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public  interface StudentRepository extends JpaRepository<StudentEntity, Long> { //Spring data repository


}
