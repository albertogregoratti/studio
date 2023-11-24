Feature: Business partner information
  Show all available business partner information including consortia relation, root institution relation, S4 mapping and CRM information (e.g. licensing manager)

  Scenario: Business partner category_name

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                    | type |
      | base_info_institution_id_2 | 2    |

    And table extraction_sap_mps_presentation.mps_bu_type contains
    # extraction_sap_mps_presentation.mps_bu_type.type (FK ->) extraction_sap_mps_presentation.mps_but000.type
      | type | text         |
      | 2    | Organization |

    Then table data_mart.b2b_business_partners should contain
    # column category_name should contain mps_bu_type.text
      | mps_partner_id             | category_name |
      | base_info_institution_id_2 | Organization  |

  Scenario: Business partner type_name

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                    | bpkind |
      | base_info_institution_id_3 | 0004   |

    And table extraction_sap_mps_presentation.mps_tb004t contains
    # extraction_sap_mps_presentation.mps_tb004t.bpkind (FK ->) extraction_sap_mps_presentation.mps_but000.bpkind
      | bpkind | text40       |
      | 0004   | Institutions |

    Then table data_mart.b2b_business_partners should contain
    # column type_name should contain mps_tb004t.text40
      | mps_partner_id             | type_name    |
      | base_info_institution_id_3 | Institutions |

  Scenario: Business partner category_id and type_id

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                    | bpkind | type |
      | base_info_institution_id_1 | 0004   | 2    |

    Then table data_mart.b2b_business_partners should contain
    # data_mart.b2b_business_partners.mps_partner_id -> extraction_sap_mps_presentation.mps_but000.partner
    # data_mart.b2b_business_partners.type_id -> extraction_sap_mps_presentation.mps_but000.bpkind
    # data_mart.b2b_business_partners.category_id -> extraction_sap_mps_presentation.mps_but000.type
      | mps_partner_id             | category_id | type_id |
      | base_info_institution_id_1 | 2           | 0004    |


  Scenario: Business partner city

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                    |
      | base_info_institution_id_4 |

    And table extraction_sap_mps_presentation.mps_but021_fs contains
    # extraction_sap_mps_presentation.mps_but021_fs.partner (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner                    | addrnumber                      | adr_kind  | valid_from     | valid_to       |
      | base_info_institution_id_4 | base_info_institution_addr_city | XXDEFAULT | 19900101125959 | 99991231125959 |

    And table extraction_sap_mps_presentation.mps_adrc contains
    # extraction_sap_mps_presentation.mps_adrc.addrnumber (FK ->) extraction_sap_mps_presentation.mps_but021_fs.addrnumber
      | addrnumber                      | city1  |
      | base_info_institution_addr_city | Berlin |

    Then table data_mart.b2b_business_partners should contain
    # column city should contain mps_adrc.city1
      | mps_partner_id             | city   |
      | base_info_institution_id_4 | Berlin |

  Scenario: Business partner region

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                    |
      | base_info_institution_id_5 |

    And table extraction_sap_mps_presentation.mps_but021_fs contains
    # extraction_sap_mps_presentation.mps_but021_fs.partner (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner                    | addrnumber                        | adr_kind  | valid_from     | valid_to       |
      | base_info_institution_id_5 | base_info_institution_addr_region | XXDEFAULT | 19900101125959 | 99991231125959 |

    And table extraction_sap_mps_presentation.mps_adrc contains
    # extraction_sap_mps_presentation.mps_adrc.addrnumber (FK ->) extraction_sap_mps_presentation.mps_but021_fs.addrnumber
    # extraction_sap_mps_presentation.mps_adrc.region (FK ->) extraction_sap_mps_presentation.mps_t005u.bland
    # extraction_sap_mps_presentation.mps_adrc.country (FK ->) extraction_sap_mps_presentation.mps_t005u.land1
      | addrnumber                        | region             | country |
      | base_info_institution_addr_region | Berlin             | DE      |

    And table extraction_sap_mps_presentation.mps_t005u contains
    # extraction_sap_mps_presentation.mps_adrc.region (FK ->)  extraction_sap_mps_presentation.mps_t005u.bland
    # extraction_sap_mps_presentation.mps_adrc.country (FK ->) extraction_sap_mps_presentation.mps_t005u.land1
      | land1 | bland  | bezei              | spras |
      | DE    | Berlin | Berlin/Brandenburg | E     |

    Then table data_mart.b2b_business_partners should contain
    # column region should contain mps_t005u.bezei where mps_t005u.spras = "E"
      | mps_partner_id             | region             |
      | base_info_institution_id_5 | Berlin/Brandenburg |


  Scenario: Business partner country

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                    |
      | base_info_institution_id_6 |

    And table extraction_sap_mps_presentation.mps_but021_fs contains
    # extraction_sap_mps_presentation.mps_but021_fs.partner (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner                    | addrnumber                         | adr_kind  | valid_from     | valid_to       |
      | base_info_institution_id_6 | base_info_institution_addr_country | XXDEFAULT | 19900101125959 | 99991231125959 |

    And table extraction_sap_mps_presentation.mps_adrc contains
    # extraction_sap_mps_presentation.mps_adrc.addrnumber (FK ->) extraction_sap_mps_presentation.mps_but021_fs.addrnumber
    # extraction_sap_mps_presentation.mps_adrc.country (FK ->) extraction_sap_mps_presentation.mps_t005t.land1
      | addrnumber                         | country |
      | base_info_institution_addr_country | DE      |

    And table extraction_sap_mps_presentation.mps_t005t contains
      | land1 | landx50 | spras |
      | DE    | Germany | E     |

    Then table data_mart.b2b_business_partners should contain
    # column country should contain mps_t005t.landx50 where mps_t005t.spras = "E"
      | mps_partner_id             | country |
      | base_info_institution_id_6 | Germany |


  Scenario: Business partner sub_region and world_region

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                    |
      | base_info_institution_id_7 |

    And table extraction_sap_mps_presentation.mps_but021_fs contains
    # extraction_sap_mps_presentation.mps_but021_fs.partner (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner                    | addrnumber                            | adr_kind  | valid_from     | valid_to       |
      | base_info_institution_id_7 | base_info_institution_addr_sub_region | XXDEFAULT | 19900101125959 | 99991231125959 |

    And table extraction_sap_mps_presentation.mps_adrc contains
    # extraction_sap_mps_presentation.mps_adrc.addrnumber (FK ->) extraction_sap_mps_presentation.mps_but021_fs.addrnumber
    # extraction_sap_mps_presentation.mps_adrc.country (FK ->) business_partners_raw.seed_bp_world_region.Value
    #   where seed_bp_world_region.Hierarchy_Level = "Country"
      | addrnumber                            | country |
      | base_info_institution_addr_sub_region | DE      |

    And world region data in present in seed business_partners_raw.seed_bp_world_region
    # "Parent" is a foreign key to itself on "Value" field (recursively)
      | Hierarchy_Level | Value      | Description                               | Parent     |
      | Country         | DE         | Germany                                   | 3020000000 |
      | Node            | 3020000000 | DACH                                      | 3000000000 |
      | Node            | 3000000000 | EMEA                                      | SN00       |
      | Root            | SN00       | Springer Nature Countries - (Inst. Sales) |            |

    Then table data_mart.b2b_business_partners should contain
    # column sub_region should contain seed_bp_world_region.Value on the recursion depth = 1 starting from Hierarchy_Level = "Country"
      | mps_partner_id             | sub_region |
      | base_info_institution_id_7 | DACH       |

    And table data_mart.b2b_business_partners should contain
    # column world_region should contain seed_bp_world_region.Value on the recursion depth = 2 starting from Hierarchy_Level = "Country"
      | mps_partner_id             | world_region |
      | base_info_institution_id_7 | EMEA         |


  Scenario: Business partner grid_id

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                    |
      | base_info_institution_id_8 |

    And table extraction_sap_mps_presentation.mps_but0id contains
    # extraction_sap_mps_presentation.mps_but0id.partner (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner                    | type  | idnumber | valid_date_from | valid_date_to |
      | base_info_institution_id_8 | ZGRID | 1        | 20000101        | 99991231      |

    Then table data_mart.b2b_business_partners should contain
    # column grid_id should contain mps_but0id.idnumber where mps_but0id.type = "ZGRID"
    # and current date is between mps_but0id.valid_date_from and mps_but0id.valid_date_to
      | mps_partner_id             | grid_id |
      | base_info_institution_id_8 | 1       |


  Scenario: Business partner name

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                     | bpkind | name_org1   | name_org2 | name_org3 | title_aca1 | title_aca2 | name_first | name_last |
      | base_info_institution_id_9  | 0001   |             |           |           | title_aca1 | title_aca2 | name_first | name_last |
      | base_info_institution_id_10 | 0004   | name part 1 | part 2    | part 3    |            |            |            |           |
      | base_info_institution_id_11 | 0007   | name part 1 | part 2    | part 3    | title_aca1 | title_aca2 | name_first | name_last |
      | base_info_institution_id_12 | 000N   | name part 1 | part 2    | part 3    | title_aca1 | title_aca2 | name_first | name_last |

    Then table data_mart.b2b_business_partners should contain concatenation of name_org1, name_org2, name_org3 for bpkind '0002', '0003', '0004' or '0005'
      | mps_partner_id              | name                      |
      | base_info_institution_id_10 | name part 1 part 2 part 3 |
    And table data_mart.b2b_business_partners should contain concatenation of title_aca1, title_aca2, name_first, name_last for bpkind '0001', '0006', 'JOUR' or 'MA'
      | mps_partner_id             | name                                       |
      | base_info_institution_id_9 | title_aca1 title_aca2 name_first name_last |
    And table data_mart.b2b_business_partners should contain name in format "<name_org1> <name_org2> <name_org3> - <title_aca1> <title_aca2> <name_first> <name_last>" for bpkind = '0007'
      | mps_partner_id              | name                                                                   |
      | base_info_institution_id_11 | name part 1 part 2 part 3 - title_aca1 title_aca2 name_first name_last |
    And table data_mart.b2b_business_partners should contain name in format "<title_aca1> <title_aca2> <name_first> <name_last> <name_org1> <name_org2> <name_org3>" for all other bpkinds
      | mps_partner_id              | name                                                                 |
      | base_info_institution_id_12 | title_aca1 title_aca2 name_first name_last name part 1 part 2 part 3 |

  Scenario: Business partner short_name

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                     | bpkind | name_org1   | name_org2 | name_org3 | title_aca1 | title_aca2 | name_first | name_last |
      | base_info_institution_id_13 | 0001   |             |           |           | title_aca1 | title_aca2 | name_first | name_last |
      | base_info_institution_id_14 | 0004   | name part 1 | part 2    | part 3    |            |            |            |           |
      | base_info_institution_id_15 | 0007   | name part 1 | part 2    | part 3    | title_aca1 | title_aca2 | name_first | name_last |
      | base_info_institution_id_16 | 000N   | name part 1 | part 2    | part 3    | title_aca1 | title_aca2 | name_first | name_last |

    Then table data_mart.b2b_business_partners should contain name_org1 for bpkind '0002', '0003', '0004' or '0005'
      | mps_partner_id              | short_name  |
      | base_info_institution_id_14 | name part 1 |
    And table data_mart.b2b_business_partners should contain concatenation of title_aca1, title_aca2, name_first, name_last for bpkind '0001', '0006', 'JOUR' or 'MA'
      | mps_partner_id              | short_name                                 |
      | base_info_institution_id_13 | title_aca1 title_aca2 name_first name_last |
    And table data_mart.b2b_business_partners should contain short_name in format "<name_first> <name_last>" for bpkind = '0007'
      | mps_partner_id              | short_name           |
      | base_info_institution_id_15 | name_first name_last |
    And table data_mart.b2b_business_partners should contain short_name in format "<title_aca1> <title_aca2> <name_first> <name_last> <name_org1> <name_org2> <name_org3>" for all other bpkinds
      | mps_partner_id              | short_name                                                           |
      | base_info_institution_id_16 | title_aca1 title_aca2 name_first name_last name part 1 part 2 part 3 |

  Scenario: Business partner organisation_name

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                     | bpkind | name_org1   | name_org2 | name_org3 | title_aca1 | title_aca2 | name_first | name_last |
      | base_info_institution_id_17 | 0001   |             |           |           | title_aca1 | title_aca2 | name_first | name_last |
      | base_info_institution_id_18 | 0004   | name part 1 | part 2    | part 3    |            |            |            |           |
      | base_info_institution_id_19 | 0007   | name part 1 | part 2    | part 3    | title_aca1 | title_aca2 | name_first | name_last |
      | base_info_institution_id_20 | 000N   | name part 1 | part 2    | part 3    | title_aca1 | title_aca2 | name_first | name_last |

    Then table data_mart.b2b_business_partners should contain concatenation of name_org1, name_org2, name_org3 for bpkind '0002', '0003', '0004' or '0005'
      | mps_partner_id              | name                      |
      | base_info_institution_id_18 | name part 1 part 2 part 3 |
    And table data_mart.b2b_business_partners should contain "null" for bpkind '0001', '0006', 'JOUR' or 'MA'
      | mps_partner_id              | organisation_name |
      | base_info_institution_id_17 | null              |
    And table data_mart.b2b_business_partners should contain concatenation of name_org1, name_org2, name_org3 for bpkind = '0007'
      | mps_partner_id              | organisation_name         |
      | base_info_institution_id_19 | name part 1 part 2 part 3 |
    And table data_mart.b2b_business_partners should contain "null" for all other bpkinds
      | mps_partner_id              | organisation_name |
      | base_info_institution_id_20 | null              |

  Scenario: Business partner s4p_partner_id

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                     | bpkind |
      | base_info_institution_id_21 | 0004   |

    And table extraction_sap_mps_presentation.mps_but0id contains
    # extraction_sap_mps_presentation.mps_but0id.partner (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner                     | type | idnumber                       | valid_date_from | valid_date_to |
      | base_info_institution_id_21 | ZS4  | base_info_s4p_institution_id_1 | 20000101        | 99991231      |

    Then table data_mart.b2b_business_partners should contain
    # column s4p_partner_id should contain mps_but0id.idnumber where mps_but0id.type = "ZS4"
    # and current date is between mps_but0id.valid_date_from and mps_but0id.valid_date_to
      | mps_partner_id              | s4p_partner_id                 |
      | base_info_institution_id_21 | base_info_s4p_institution_id_1 |

  Scenario: Business partner s4p_partner_name

    Given Business partner is created in MPS

    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                     | bpkind |
      | base_info_institution_id_22 | 0004   |

    And table extraction_sap_mps_presentation.mps_but0id contains
    # extraction_sap_mps_presentation.mps_but0id.partner (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner                     | type | idnumber                  | valid_date_from | valid_date_to |
      | base_info_institution_id_22 | ZS4  | base_info_s4p_org_id_1    | 20000101        | 99991231      |
      | base_info_institution_id_22 | ZS4  | base_info_s4p_person_id_1 | 20000101        | 99991231      |

    And table extraction_sap_s4p_presentation.s4p_but000 contains
    # extraction_sap_s4p_presentation.s4p_but000.partner (FK ->) extraction_sap_mps_presentation.mps_but0id.idnumber
      | partner                   | type | title_aca1 | title_aca2 | name_first | name_last | name_org1 | name_org2 | name_org3 | name_org4 |
      | base_info_s4p_org_id_1    | 2    |            |            |            |           | name_org1 | name_org2 | name_org3 | name_org4 |
      | base_info_s4p_person_id_1 | 1    | title_aca1 | title_aca2 | name_first | name_last |           |           |           |           |

    Then table data_mart.b2b_business_partners should contain for organisation concatenation of fields name_org1, name_org2, name_org3 and name_org4 from extraction_sap_s4p_presentation.s4p_but000
    # column s4p_partner_id should contain mps_but0id.idnumber where mps_but0id.type = "ZS4"
    # and current date is between mps_but0id.valid_date_from and mps_but0id.valid_date_to
    # and extraction_sap_s4p_presentation.s4p_but000.type = 2
      | mps_partner_id              | s4p_partner_name                        |
      | base_info_institution_id_22 | name_org1 name_org2 name_org3 name_org4 |
    And table data_mart.b2b_business_partners should contain for persons concatenation of fields title_aca1, title_aca2, name_first and name_last from extraction_sap_s4p_presentation.s4p_but000
    # column s4p_partner_id should contain mps_but0id.idnumber where mps_but0id.type = "ZS4"
    # and current date is between mps_but0id.valid_date_from and mps_but0id.valid_date_to
    # and extraction_sap_s4p_presentation.s4p_but000.type = 1
      | mps_partner_id              | s4p_partner_name                           |
      | base_info_institution_id_22 | title_aca1 title_aca2 name_first name_last |

  Scenario: Salesforce information
    Given Business partner is created in Salesforce
    And table extraction_sap_mps_presentation.mps_but000 contains
      | partner                   |
      | crm_info_institution_id_1 |
    And table ces---data-pipelines-ffeaa78d.SF_DataViews.Account_DataView contains
    # ces---data-pipelines-ffeaa78d.SF_DataViews.Account_DataView.sap_id (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | sap_id                    | channel_type | customer_type | account_id | account_name |
      | crm_info_institution_id_1 | Academic     | Pharma        | SF-Acc-1   | SF Acc Name  |
    And table ces---data-pipelines-ffeaa78d.SF_DataViews.SFID_BPID_DataView contains
    # ces---data-pipelines-ffeaa78d.SF_DataViews.SFID_BPID_DataView.sap_id__c (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | sap_id__c                 | licensing_manager      | vice_president      |
      | crm_info_institution_id_1 | licensing manager name | vice president name |

    Then table data_mart.b2b_business_partners should contain
      | mps_partner_id            | channel_type | customer_type | salesforce_account_id | salesforce_account_name | licensing_manager_name | vice_president_name |
      | crm_info_institution_id_1 | Academic     | Pharma        | SF-Acc-1              | SF Acc Name             | licensing manager name | vice president name |
    # Mapping:
    # mps_partner_id          -> extraction_sap_mps_presentation.mps_but000.partner
    # channel_type            -> ces---data-pipelines-ffeaa78d.SF_DataViews.Account_DataView.channel_type
    # customer_type           -> ces---data-pipelines-ffeaa78d.SF_DataViews.Account_DataView.customer_type
    # salesforce_account_id   -> ces---data-pipelines-ffeaa78d.SF_DataViews.Account_DataView.account_id
    # salesforce_account_name -> ces---data-pipelines-ffeaa78d.SF_DataViews.Account_DataView.account_name
    # licensing_manager_name  -> ces---data-pipelines-ffeaa78d.SF_DataViews.SFID_BPID_DataView.licensing_manager
    # vice_president_name     -> ces---data-pipelines-ffeaa78d.SF_DataViews.SFID_BPID_DataView.vice_president

  Scenario: Consortia relation
    Given the consortia relationship is set up in mps
    And table extraction_sap_mps_presentation.mps_but000 contains consortia partner with bpkind = '0005'
      | partner              | bpkind |
      | cons_rel_consortia_1 | 0005   |
    And table extraction_sap_mps_presentation.mps_but000 contains institute partner with bpkind = '0004'
      | partner              | bpkind |
      | cons_rel_institute_1 | 0004   |
    And table extraction_sap_mps_presentation.mps_but050 contains
    # extraction_sap_mps_presentation.mps_but050.partner1 (FK ->) extraction_sap_mps_presentation.mps_but000.partner
    # extraction_sap_mps_presentation.mps_but050.partner2 (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner1             | partner2             | date_from | date_to  | reltyp | relkind |
      | cons_rel_consortia_1 | cons_rel_institute_1 | 20000101  | 99991231 | BUR002 | INST    |
    Then table data_mart.b2b_business_partners should contain column consortia_id to display to which consortia given mps_partner_id belongs
    # consortia_id is mps_but050.partner1 with corresponding mps_but000.bpkind = '0005'
    # mps_partner_id is mps_but050.partner2 with corresponding mps_but000.bpkind = '0004'
    # and current date is between mps_but050.date_from and mps_but050.date_to
    # and mps_but050.reltyp = 'BUR002'
    # and mps_but050.relkind = 'INST'
      | mps_partner_id       | consortia_id         |
      | cons_rel_institute_1 | cons_rel_consortia_1 |
      | cons_rel_consortia_1 | cons_rel_consortia_1 |
    And table data_mart.b2b_business_partners should contain column is_consortia to display if mps_partner_id is consortia
    # mps_partner_id is extraction_sap_mps_presentation.mps_but000
    # and is_consortia = 'true' if mps_but000.bpkind = '0005'
      | mps_partner_id       | is_consortia |
      | cons_rel_institute_1 | false        |
      | cons_rel_consortia_1 | true         |

  Scenario: Root Institution relation
    Given the root institution relationship is set up in mps
    And table extraction_sap_mps_presentation.mps_but000 contains root institution partner with bpkind = '0004'
      | partner              | bpkind |
      | root_rel_root_inst_1 | 0004   |
    And table extraction_sap_mps_presentation.mps_but000 contains institute partner with bpkind = '0004'
      | partner         | bpkind |
      | root_rel_inst_1 | 0004   |
    And table extraction_sap_mps_presentation.mps_but050 contains
    # extraction_sap_mps_presentation.mps_but050.partner1 (FK ->) extraction_sap_mps_presentation.mps_but000.partner
    # extraction_sap_mps_presentation.mps_but050.partner2 (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner1             | partner2        | date_from | date_to  | reltyp | relkind |
      | root_rel_root_inst_1 | root_rel_inst_1 | 20000101  | 99991231 | BUR002 | INST    |
    Then table data_mart.b2b_business_partners should contain column root_institution_id to show to which root institution given mps_partner_id belongs
    # root_institution_id is mps_but050.partner1 with corresponding mps_but000.bpkind = '0004'
    # mps_partner_id is mps_but050.partner2 with corresponding mps_but000.bpkind = '0004'
    # and current date is between mps_but050.date_from and mps_but050.date_to
    # and mps_but050.reltyp = 'BUR002'
    # and mps_but050.relkind = 'INST'
      | mps_partner_id       | root_institution_id  |
      | root_rel_inst_1      | root_rel_root_inst_1 |
      | root_rel_root_inst_1 | root_rel_root_inst_1 |
    And table data_mart.b2b_business_partners should contain column is_root_institution to show if mps_partner_id is root institution to other istitutions
    # mps_partner_id is extraction_sap_mps_presentation.mps_but000
    # and is_root_institution = 'true' if mps_partner_id = root_institution_id
      | mps_partner_id       | root_institution_id  | is_root_institution |
      | root_rel_inst_1      | root_rel_root_inst_1 | false               |
      | root_rel_root_inst_1 | root_rel_root_inst_1 | true                |

  Scenario: Head of Account
    Given the institution relationship is set up in mps
    And table extraction_sap_mps_presentation.mps_but000 contains root institution partner
      | partner         | bpkind |
      | rel_root_inst_1 | 0004   |
      | rel_root_inst_2 | 0004   |
    And table extraction_sap_mps_presentation.mps_but050 contains
    # extraction_sap_mps_presentation.mps_but050.partner1 (FK ->) extraction_sap_mps_presentation.mps_but000.partner
    # extraction_sap_mps_presentation.mps_but050.partner2 (FK ->) extraction_sap_mps_presentation.mps_but000.partner
      | partner1        | partner2        | date_from | date_to  | reltyp | relkind |
      | rel_root_inst_1 | rel_root_inst_2 | 20000101  | 99991231 | BUR002 | INST    |
    Then table data_mart.b2b_business_partners should contain column mps_head_of_account_id to display head of account id for given mps_partner_id
    # mps_head_of_account_id is mps_but050.partner1
    # mps_partner_id is mps_but050.partner2
    # and current date is between mps_but050.date_from and mps_but050.date_to
      | mps_partner_id  | mps_head_of_account_id |
      | rel_root_inst_2 | rel_root_inst_1        |
      | rel_root_inst_1 | null                   |

  Scenario: Email Domain
    # For marketing, we need to identify to which institution the business partner could belong with the help of the email domain
    # Ticket https://app.shortcut.com/projectdata/story/17051/add-email-domain-to-the-business-partners-table

    Given business partner exists in the MPS system
      | mps_partner_id      |
      | person_partner_id_1 |

    And table "extraction_sap_mps_presentation.mps_but021_fs" contains field "PARTNER" which refers to mps_partner_id
      | PARTNER             | ADDRNUMBER               |
      | person_partner_id_1 | addr_person_partner_id_1 |

    And table "extraction_sap_mps_presentation.mps_adr6" contains field "ADDRNUMBER" which is FK to the "mps_but021_fs.ADDRNUMBER"
      | ADDRNUMBER               | SMTP_ADDR                                     | FLGDEFAULT | PERSNUMBER | record_metadata                    |
      | addr_person_partner_id_1 | addr_person_partner_id_1@institution_id_1.com | X          |            | {"exists_in_source_system": true}  |
      | addr_person_partner_id_2 | addr_person_partner_id_2@institution_id_1.com | Y          |            | {"exists_in_source_system": false} |

    Then table "data_mart.b2b_business_partners" column "email_domain" should email domain part from "mps_adr6.SMTP_ADDR" for all types of business partners where "mps_adr6.FLGDEFAULT" = "X" AND "mps_adr6.PERSNUMBER" = " " AND "mps_adr6.record_metadata.exists_in_source_system" is TRUE
      | mps_partner_id      | email_domain         |
      | person_partner_id_1 | institution_id_1.com |

    Then table "business_partners_presentation.business_partners" column "email_domain" should email domain part from "mps_adr6.SMTP_ADDR" for all types of business partners  where "mps_adr6.FLGDEFAULT" = "X" AND "mps_adr6.PERSNUMBER" = " " AND "mps_adr6.record_metadata.exists_in_source_system" is TRUE
      | mps_partner_id      | email_domain         |
      | person_partner_id_1 | institution_id_1.com |
