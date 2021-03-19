//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.cockroach.repository;

import com.example.helloworldservice.cockroach.model.LanguageRow;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface LanguagesRepository extends JpaRepository<LanguageRow, UUID> {
}