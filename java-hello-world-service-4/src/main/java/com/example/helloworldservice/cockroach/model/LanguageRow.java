//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.cockroach.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder(toBuilder = true)
@Entity
@Table(indexes = {@Index(name = "language_name_idx", columnList = "name", unique = true)})
public class LanguageRow {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private UUID languageId;

    @Column(length = 128)
    private String name;

    @Column(length = 512)
    private String description;
}