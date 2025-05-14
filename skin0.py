#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/DrMundo/DrMundo.bin"
    "DATA/Characters/DrMundo/Animations/Skin0.bin"
    "DATA/DrMundo_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/DrMundo_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin7_Skins_Skin9.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin20_Skins_Skin3_Skins_Skin5_Skins_Skin7.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin7.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin7_Skins_Skin9.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin7_Skins_Skin8.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin7.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin4_Skins_Skin5.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin5.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2.bin"
    "DATA/Characters/DrMundo/DrMundo.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/DrMundo/Animations/Skin0.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/DrMundo_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin5_Skins_Skin6_Skins_Skin8_Skins_Skin9.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin9.bin"
    "DATA/DrMundo_Skins_Skin0_Skins_Skin1_Skins_Skin2.bin"
}
entries: map[hash,embed] = {
    "Characters/DrMundo/Skins/Skin0" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "BaseDrMundo"
        metaDataTags: string = "faction:zaun,gender:male,race:human"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/DrMundo/Skins/Base/DrMundoLoadscreen_0.dds"
        }
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "DrMundo"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "DrMundo_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/DrMundo/Skins/Base/DrMundo_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/DrMundo/Skins/Base/DrMundo_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/DrMundo/Skins/Base/DrMundo_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_DrMundo_AttackChampion2D"
                        "Play_vo_DrMundo_Death3D"
                        "Play_vo_DrMundo_DrMundoBasicAttack2_cast3D"
                        "Play_vo_DrMundo_DrMundoCritAttack_cast3D"
                        "Play_vo_DrMundo_InfectedCleaverMissileCast_cast3D"
                        "Play_vo_DrMundo_Joke3DGeneral"
                        "Play_vo_DrMundo_Laugh3DGeneral"
                        "Play_vo_DrMundo_MoveOrder2D"
                        "Play_vo_DrMundo_Taunt3DGeneral"
                    }
                    voiceOver: bool = true
                }
                BankUnit {
                    name: string = "DrMundo_Base_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/DrMundo/Skins/Base/DrMundo_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/DrMundo/Skins/Base/DrMundo_Base_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_DrMundo_Dance3D_cast"
                        "Play_sfx_DrMundo_Dance3D_loop"
                        "Play_sfx_DrMundo_Death3D_cast"
                        "Play_sfx_DrMundo_DrMundoBasicAttack2_OnCast"
                        "Play_sfx_DrMundo_DrMundoBasicAttack2_OnHit"
                        "Play_sfx_DrMundo_DrMundoBasicAttack3_OnCast"
                        "Play_sfx_DrMundo_DrMundoBasicAttack3_OnHit"
                        "Play_sfx_DrMundo_DrMundoBasicAttack_OnCast"
                        "Play_sfx_DrMundo_DrMundoBasicAttack_OnHit"
                        "Play_sfx_DrMundo_DrMundoBasicAttackTower_OnCast"
                        "Play_sfx_DrMundo_DrMundoBasicAttackTower_OnHit"
                        "Play_sfx_DrMundo_DrMundoCritAttack_OnCast"
                        "Play_sfx_DrMundo_DrMundoCritAttack_OnHit"
                        "Play_sfx_DrMundo_DrMundoE_OnBuffActivate"
                        "Play_sfx_DrMundo_DrMundoE_OnBuffDeactivate"
                        "Play_sfx_DrMundo_DrMundoE_OnCast"
                        "Play_sfx_DrMundo_DrMundoEAttack_cast"
                        "Play_sfx_DrMundo_DrMundoEAttack_OnHit"
                        "Play_sfx_DrMundo_DrMundoEMissile_end"
                        "Play_sfx_DrMundo_DrMundoEMissile_hit"
                        "Play_sfx_DrMundo_DrMundoEMissile_missilelaunch"
                        "Play_sfx_DrMundo_DrMundoPImmunity_OnBuffActivate"
                        "Play_sfx_DrMundo_DrMundoPImmunity_OnBuffDeactivate"
                        "Play_sfx_DrMundo_DrMundoPObject_break"
                        "Play_sfx_DrMundo_DrMundoPObject_land"
                        "Play_sfx_DrMundo_DrMundoPObject_missilelaunch"
                        "Play_sfx_DrMundo_DrMundoPObject_pickup"
                        "Play_sfx_DrMundo_DrMundoQ_hit_ground"
                        "Play_sfx_DrMundo_DrMundoQ_OnCast"
                        "Play_sfx_DrMundo_DrMundoQ_OnHit"
                        "Play_sfx_DrMundo_DrMundoQ_OnMissileLaunch"
                        "Play_sfx_DrMundo_DrMundoR_OnBuffActivate"
                        "Play_sfx_DrMundo_DrMundoR_OnBuffDeactivate"
                        "Play_sfx_DrMundo_DrMundoR_OnCast"
                        "Play_sfx_DrMundo_DrMundoW_buffdeactivate"
                        "Play_sfx_DrMundo_DrMundoW_heal_buffactivate"
                        "Play_sfx_DrMundo_DrMundoW_hit"
                        "Play_sfx_DrMundo_DrMundoW_OnBuffActivate"
                        "Play_sfx_DrMundo_DrMundoW_OnCast"
                        "Play_sfx_DrMundo_IdleVar2_buffactivate"
                        "Play_sfx_DrMundo_Joke3D_buffactivate"
                        "Play_sfx_DrMundo_Laugh3D_buffactivate"
                        "Play_sfx_DrMundo_Recall3D_buffactivate"
                        "Play_sfx_DrMundo_Respawn3D_buffactivate"
                        "Play_sfx_DrMundo_Taunt3D_buffactivate"
                        "Play_sfx_DrMundo_Winddown3D_buffactivate"
                        "Stop_sfx_DrMundo_DrMundoE_OnBuffActivate"
                        "Stop_sfx_DrMundo_DrMundoPImmunity_OnBuffActivate"
                        "Stop_sfx_DrMundo_DrMundoPObject_missilelaunch"
                        "Stop_sfx_DrMundo_DrMundoQ_OnMissileLaunch"
                        "Stop_sfx_DrMundo_DrMundoR_OnBuffActivate"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/DrMundo/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/DrMundo/Skins/Base/DrMundo_Base.skl"
            simpleSkin: string = "ASSETS/Characters/DrMundo/Skins/Base/DrMundo_Base.skn"
            texture: string = "ASSETS/Characters/DrMundo/Skins/Base/DrMundo_Base_TX_CM.dds"
            skinScale: f32 = 0.949999988
            selfIllumination: f32 = 0.699999988
            overrideBoundingBox: option[vec3] = {
                { 250, 300, 250 }
            }
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Flesh"
        mContextualActionData: link = "Characters/DrMundo/CAC/DrMundo_Base"
        iconCircle: option[string] = {
            "ASSETS/Characters/DrMundo/HUD/DrMundo_Circle_0.dds"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/DrMundo/HUD/DrMundo_Square_0.dds"
        }
        mResourceResolver: link = "Characters/DrMundo/Skins/Skin0/Resources"
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 12
        }
    }
    "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Ground_Enemy" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.0235294122, 0.0392156877, 0.992156863 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.235294119, 0.13333334, 0.388235301, 1 }
                            { 0.23137255, 0.137254909, 0.290196091, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 200, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, -100 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Ziggs/Skins/Base/Particles/Ziggs_Base_R_SoftCircle.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.188235298, 0.0156862754, 0.0941176489, 0.772549033 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.235294119, 0.13333334, 0.388235301, 1 }
                            { 0.23137255, 0.137254909, 0.290196091, 0 }
                        }
                    }
                }
                pass: i16 = -20
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, -100 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Ziggs/Skins/Base/Particles/Ziggs_Base_R_SoftCircle.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    6
                }
                emitterName: string = "Shapes"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 40, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 100 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 100 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[f32] = {
                            0
                            0
                            0
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.719996929, 0.379995435, 0.960006118, 0.549996197 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.549019635, 0.882352948, 1, 0.505882382 }
                            { 0.75686276, 0.545098066, 1, 1 }
                            { 0.784313738, 0.345098048, 1, 0.498039216 }
                            { 0.419607848, 0.0823529437, 1, 0 }
                        }
                    }
                }
                pass: i16 = 600
                alphaRef: u8 = 130
                softParticleParams: pointer = VfxSoftParticleDefinitionData {}
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.50999999
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    4
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 80, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.900000036, 0.5, 1 }
                            { 0.75, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/Illaoi_Base_E_IdolShapes.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    6
                }
                emitterName: string = "Shapes1"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 40, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 80, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 80, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 100 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 100 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[f32] = {
                            0
                            0
                            0
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.835294187, 0.835294187, 0.835294187, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.549996197, 0.880003035, 1, 0 }
                            { 0.458823532, 0.929411769, 1, 1 }
                            { 0.345098048, 0.913725495, 1, 1 }
                            { 0.419607848, 0.0823529437, 1, 0 }
                        }
                    }
                }
                pass: i16 = 600
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_R_Bubble_Erode.dds"
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.50999999
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 80, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.5
                            0.772540033
                            0.851258576
                            0.897025168
                            0.935926795
                            0.980000019
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.25, 0, 0 }
                            { 0.75, 1, 1 }
                            { 1.13157892, 0, 0 }
                            { 0.934210539, 0, 0 }
                            { 1.01315784, 0, 0 }
                            { 0.881578922, 0, 0 }
                            { 0.850000024, 0, 0 }
                            { 1.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_GroundGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.530006886 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.733333349, 0.0901960805, 0.239215687, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.733333349, 0.0901960805, 0.239215687, 0 }
                            { 0.23294118, 0.086658977, 0.207320258, 1 }
                            { 0.16104576, 0.0785236433, 0.156662822, 1 }
                            { 0.04026144, 0.000353710144, 0.0225144178, 0 }
                        }
                    }
                }
                pass: i16 = -10
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.75, 0, 0 }
                            { 0.75, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Backdrop.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    6
                }
                emitterName: string = "Temp_GroundGlow1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 0, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 0, 30 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 0, 30 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.549996197 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.113725491, 0.392156869, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.340000004
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.113725491, 0.392156869, 0 }
                            { 0.431372553, 0.0388004631, 0.370626688, 1 }
                            { 0.0549019612, 0.000445982354, 0.0369088836, 0 }
                        }
                    }
                }
                pass: i16 = -2
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 270, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 10, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.637500048, 0, 0 }
                            { 0.75, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Backdrop.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Ripple_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.669993162 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.180392161, 0.764705896, 0.647058845, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.180392161, 0.764705896, 0.647058845, 0 }
                            { 0.180392161, 0.764705896, 0.647058845, 1 }
                            { 0.180392161, 0.764705896, 0.647058845, 1 }
                            { 0.0141484048, 0.188927338, 0.124336801, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.949999988
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.129999995
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Chemical_Mult.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Gradients_Blur.dds"
                    PaletteTextureAddressMode: u8 = 0
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 0, 1 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                    }
                    PaletteUAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                2
                            }
                        }
                    }
                    PaletteVAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 2
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                2
                                2
                            }
                        }
                    }
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.200000003 }
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    6.5
                }
                emitterName: string = "Temp_Mesh1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Ripple_Mesh.scb"
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.379995435 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.498039216, 0.850980401, 0.905882359, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.320588231
                            0.514705896
                            0.70588237
                            1
                        }
                        values: list[vec4] = {
                            { 0.498039216, 0.850980401, 0.905882359, 0 }
                            { 0.498039216, 0.850980401, 0.905882359, 1 }
                            { 0.397492468, 0.710615873, 0.745566845, 0.327868849 }
                            { 0.295083731, 0.567651927, 0.582282484, 0.639344275 }
                            { 0.194226667, 0.426854223, 0.421472102, 0.180327863 }
                            { 0.0390619002, 0.210242212, 0.174071521, 0 }
                        }
                    }
                }
                pass: i16 = 8
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.850000024
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.340000004
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_W_LightningErosion03.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Lightning03.dds"
                frameRate: f32 = 5
                numFrames: u16 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.200000003 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
                texDiv: vec2 = { 2, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.50999999
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 2, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Lightning_disk.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.319996953 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.109803922, 0.121568628, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.109803922, 0.121568628, 0 }
                            { 1, 0.109803922, 0.121568628, 1 }
                            { 1, 0.109803922, 0.121568628, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = -40
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                uvScrollClampMult: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4.5, 5, 6 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_Shield_Inner_Mult.dds"
                startFrame: u16 = 1
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.200000003 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -90
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/common_color-rampdown.dds"
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
                }
                texAddressModeMult: u8 = 2
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { -1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh3"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_PuddleMesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.530006886 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.529411793, 0.286274523, 0.827450991, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.529411793, 0.286274523, 0.827450991, 0 }
                            { 0.529411793, 0.286274523, 0.827450991, 1 }
                            { 0.529411793, 0.286274523, 0.827450991, 1 }
                            { 0.0415224917, 0.0707266405, 0.159000382, 0 }
                        }
                    }
                }
                pass: i16 = -4
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                0.949999988
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.129999995
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "alpha puddle"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_PuddleMesh.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.478431374, 0.239215687, 0.615686297, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.478431374, 0.239215687, 0.615686297, 0 }
                            { 0.478431374, 0.239215687, 0.615686297, 1 }
                            { 0.478431374, 0.239215687, 0.615686297, 1 }
                            { 0.0375240296, 0.0591003448, 0.118308343, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                0.949999988
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.129999995
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh5"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubblemesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.439993888 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.53725493, 0.403921574, 0.866666675, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.53725493, 0.403921574, 0.866666675, 0 }
                            { 0.53725493, 0.403921574, 0.866666675, 1 }
                            { 0.53725493, 0.403921574, 0.866666675, 1 }
                            { 0.0421376415, 0.0997923911, 0.166535944, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.25
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.340000004
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble_Mesh_Erode.dds"
                }
                disableBackfaceCull: bool = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.649999976, 1, 0.649999976 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.449526817
                            0.602193058
                            0.680911601
                            0.726678193
                            0.787661791
                            0.854889572
                            0.980000019
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.324999988, 1, 0.324999988 }
                            { 0.496052623, 1.01315784, 0.495950013 }
                            { 0.752631545, 1.15799999, 0.752699971 }
                            { 0.624342144, 0.961000025, 0.624650002 }
                            { 0.675657868, 1.03900003, 0.67535001 }
                            { 0.538815796, 0.828999996, 0.538850009 }
                            { 0.667105258, 1.02600002, 0.666900039 }
                            { 0.55250001, 2, 0.55250001 }
                            { 0.324999988, 0, 0.324999988 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubble_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.850000024
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    6
                }
                emitterName: string = "Temp_Mesh6"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 80, 0, 80 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 80, 0, 80 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubblemesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.570000768 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.570000768 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.380392164, 0.34117648, 0.90196079, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.380392164, 0.34117648, 0.90196079, 0 }
                            { 0.380392164, 0.34117648, 0.90196079, 1 }
                            { 0.380392164, 0.34117648, 0.90196079, 1 }
                            { 0.0298346803, 0.0842906609, 0.173317954, 0 }
                        }
                    }
                }
                pass: i16 = 48
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.25
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.340000004
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble_Mesh_Erode.dds"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 5, 1 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.449526817
                            0.602193058
                            0.680911601
                            0.726678193
                            0.787661791
                            0.854889572
                            0.980000019
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.1875, 0, 0 }
                            { 0.572368443, 1.01315784, 1.01315784 }
                            { 0.868421078, 0, 0 }
                            { 0.720394731, 0, 0 }
                            { 0.779605269, 0, 0 }
                            { 0.621710539, 0, 0 }
                            { 0.769736886, 0, 0 }
                            { 0.637500048, 0, 0 }
                            { 1.125, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubble_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    6
                }
                emitterName: string = "Temp_Mesh7"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 80, 0, 80 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 80, 0, 80 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubblemesh.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.540001512 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0.435294122, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.549019635, 0.435294122, 1, 0 }
                            { 0.549019635, 0.435294122, 1, 1 }
                            { 0.549019635, 0.435294122, 1, 1 }
                            { 0.0430603623, 0.107543252, 0.192156866, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.25
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.340000004
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble_Mesh_Erode.dds"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 5, 1 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.449526817
                            0.602193058
                            0.680911601
                            0.726678193
                            0.787661791
                            0.854889572
                            0.980000019
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.1875, 0, 0 }
                            { 0.572368443, 1.01315784, 1.01315784 }
                            { 0.868421078, 0, 0 }
                            { 0.720394731, 0, 0 }
                            { 0.779605269, 0, 0 }
                            { 0.621710539, 0, 0 }
                            { 0.769736886, 0, 0 }
                            { 0.637500048, 0, 0 }
                            { 1.125, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubble_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Ray"
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.97999543 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.34117648, 0.227450982, 0.43921569, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.34117648, 0.227450982, 0.43921569, 0 }
                            { 0.34117648, 0.227450982, 0.43921569, 1 }
                            { 0.34117648, 0.227450982, 0.43921569, 0 }
                        }
                    }
                }
                uvScrollClampMult: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 50 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 0.75, 0.75 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.75, 0.75, 0.75 }
                            { 0.75, 1.125, 0.75 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Smokey_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Ray_Mult.dds"
                texAddressModeMult: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh8"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Funnel_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.90196079, 0.549019635, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.90196079, 0.549019635, 1, 0 }
                            { 0.90196079, 0.549019635, 1, 1 }
                            { 0.90196079, 0.549019635, 1, 1 }
                            { 0.16978085, 0.103344873, 0.188235298, 0 }
                        }
                    }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 9, 3, 9 }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Chemical_Mult.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.649999976 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            4
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.25
                }
                lifetime: option[f32] = {
                    4
                }
                emitterName: string = "Temp_Ray1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -20, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 125, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 125, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.340001523 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.340001523 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.635294139, 0.321568638, 0.992156863, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.635294139, 0.321568638, 0.992156863, 0 }
                            { 0.635294139, 0.321568638, 0.992156863, 1 }
                            { 0.0921799317, 0.0302652828, 0.303483278, 0.56078434 }
                            { 0.191833913, 0.0971011147, 0.299592465, 0 }
                        }
                    }
                }
                pass: i16 = 45
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_Ground_Trail_Erode.dds"
                }
                miscRenderFlags: u8 = 1
                uvScrollAlphaMult: flag = false
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 300, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 300, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 0.75, 0.75 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.75, 0.337499976, 0.75 }
                            { 0.375, 0.75, 0.75 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 1 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Cas_Ground_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                texAddressModeMult: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh9"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Ripple_Mesh.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.650003791 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.58431375, 0.23137255, 0.607843161, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.58431375, 0.23137255, 0.607843161, 0 }
                            { 0.58431375, 0.23137255, 0.607843161, 1 }
                            { 0.58431375, 0.23137255, 0.607843161, 0.519996941 }
                            { 0.0458285324, 0.0571626313, 0.11680124, 0 }
                        }
                    }
                }
                pass: i16 = -2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.949999988
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.129999995
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Chemical_Mult.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Gradients_Blur.dds"
                    PaletteTextureAddressMode: u8 = 0
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 0, 0.540001512 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                    }
                    PaletteUAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 2
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                2
                            }
                        }
                    }
                    PaletteVAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 0.5
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 2 }
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh10"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -40, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Funnel_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.596078455, 0.164705887, 0.737254918, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.596078455, 0.164705887, 0.737254918, 0 }
                            { 0.596078455, 0.164705887, 0.737254918, 1 }
                            { 0.596078455, 0.164705887, 0.737254918, 1 }
                            { 0.112203002, 0.0310034603, 0.13877739, 0 }
                        }
                    }
                }
                pass: i16 = 40
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble_Mesh_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 6, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0, 0.300000012 }
                            { 1, 2, 1 }
                            { 2, 0, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Goop.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, -1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh12"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Funnel_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.439993888 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.474509805, 0.164705887, 0.529411793, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.474509805, 0.164705887, 0.529411793, 0 }
                            { 0.474509805, 0.164705887, 0.529411793, 1 }
                            { 0.474509805, 0.164705887, 0.529411793, 1 }
                            { 0.0893194973, 0.0310034603, 0.0996539816, 0 }
                        }
                    }
                }
                pass: i16 = -20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.850000024
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.25
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 9, 0, 9 }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Goop.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.400000006 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                isSingleParticle: flag = true
                emitterName: string = "Beaker"
                Linger: pointer = VfxLingerDefinitionData {
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.941176474, 0.941176474, 0.941176474, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skl"
                        mAnimationName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_CanisterIdle.anm"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Ziggs/Skins/Skin01/Particles/color-hold.DDS"
                blendMode: u8 = 3
                pass: i16 = 20
                censorModulateValue: vec4 = { 0.909803927, 0.925490201, 0.905882359, 1 }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.647058845, 0.243137255, 1, 1 }
                    fresnel: f32 = 0.5
                    fresnelColor: vec4 = { 0.211764708, 0.0549019612, 0.337254912, 0 }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                doesCastShadow: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -12 }
                            { 0, 0, -12 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 1.29999995, 1.29999995 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/DrMundo_Base_Weapon_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                isSingleParticle: flag = true
                emitterName: string = "Beaker1"
                Linger: pointer = VfxLingerDefinitionData {
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.941176474, 0.941176474, 0.941176474, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skl"
                        mAnimationName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_CanisterIdle.anm"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Ziggs/Skins/Skin01/Particles/color-hold.DDS"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.129999995
                            0.349999994
                            0.649999976
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.984313726, 0.43921569, 1 }
                            { 0.423529416, 0.266666681, 0.105882354, 0 }
                            { 1, 0.972549021, 0.152941182, 1 }
                            { 0.349019617, 0.258823544, 0.117647059, 0 }
                            { 1, 0.905882359, 0.180392161, 1 }
                            { 0.196078435, 0.0941176489, 0.0235294122, 0 }
                        }
                    }
                }
                pass: i16 = 25
                censorModulateValue: vec4 = { 0.909803927, 0.925490201, 0.905882359, 1 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -12 }
                            { 0, 0, -12 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/3161color-hold.TFT_Booms_Set7_5.dds"
            }
        }
        particleName: string = "DrMundo_Base_P_Cannister_Ground_Enemy"
        particlePath: string = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Ground_Enemy"
        soundPersistentDefault: string = "Play_sfx_DrMundo_DrMundoPObject_land"
        flags: u8 = 212
    }
    "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Missile" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 11
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "DrMundo_P_Cannister_Trail_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "Capacitor"
                    }
                }
                emitterName: string = "Beaker"
                Linger: pointer = VfxLingerDefinitionData {
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.941176474, 0.941176474, 0.941176474, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skl"
                        mAnimationName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Canister.anm"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Ziggs/Skins/Skin01/Particles/color-hold.DDS"
                blendMode: u8 = 3
                pass: i16 = 20
                censorModulateValue: vec4 = { 0.909803927, 0.925490201, 0.905882359, 1 }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.647058845, 0.243137255, 1, 1 }
                    fresnel: f32 = 0.5
                    fresnelColor: vec4 = { 0.211764708, 0.0549019612, 0.337254912, 0 }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                doesCastShadow: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 1.29999995, 1.29999995 }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/DrMundo_Base_Weapon_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Beaker1"
                Linger: pointer = VfxLingerDefinitionData {
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.941176474, 0.941176474, 0.941176474, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Canister.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Canister.skl"
                        mAnimationName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Canister.anm"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Ziggs/Skins/Skin01/Particles/color-hold.DDS"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.480003059 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.984313726, 0.43921569, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 25
                censorModulateValue: vec4 = { 0.909803927, 0.925490201, 0.905882359, 1 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 1, 1 }
                }
                texture: string = "ASSETS/Shared/Particles/3161color-hold.TFT_Booms_Set7_5.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    12
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_GroundGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.130006865 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.866666675, 0.180392161, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.866666675, 0.180392161, 1, 0 }
                            { 0.866666675, 0.180392161, 1, 1 }
                            { 0.866666675, 0.180392161, 1, 1 }
                            { 0.0543790832, 0.00919646304, 0.0941176489, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/bigglow02.TFT_Set7.dds"
            }
        }
        particleName: string = "DrMundo_Base_P_Cannister_Missile"
        particlePath: string = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Missile"
        soundPersistentDefault: string = "Play_sfx_DrMundo_DrMundoPObject_missilelaunch"
        flags: u8 = 212
    }
    "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_Bonesaw_Child" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {}
        particleName: string = "DrMundo_Base_Q_Bonesaw_Child"
        particlePath: string = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_Bonesaw_Child"
        soundOnCreateDefault: string = "Play_sfx_DrMundo_DrMundoQ_hit_ground"
    }
    "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Crush" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 80
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    0.150000006
                }
                isSingleParticle: flag = true
                emitterName: string = "blood_02"
                importance: u8 = 0
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0.300000012 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 800, 400 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 800, 400 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 10, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.137254909, 0.274509817, 0.423529416, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.853999972
                            1
                        }
                        values: list[vec4] = {
                            { 0.137254909, 0.274509817, 0.423529416, 0 }
                            { 0.137254909, 0.274509817, 0.423529416, 1 }
                            { 0.137254909, 0.274509817, 0.423529416, 1 }
                            { 0.137254909, 0.274509817, 0.423529416, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
                }
                directionVelocityScale: f32 = 0.00800000038
                directionVelocityMinScale: f32 = 0.200000003
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.383177578
                            0.528037369
                            0.65420562
                            0.803738296
                            0.850467265
                            0.948598146
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.582352936, 0.708991289, 0.708991289 }
                            { 0.617647052, 0.542485774, 0.542485774 }
                            { 0.429411769, 0.397464812, 0.397464812 }
                            { 0.552941203, 0.225588143, 0.225588143 }
                            { 0.323529422, 0.171876684, 0.171876684 }
                            { 0.411764711, 0.0590826087, 0.0590826087 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/Wukong_Base_Sparkles.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    0.150000006
                }
                isSingleParticle: flag = true
                emitterName: string = "blood_4"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 200, 500 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 500, 200, 500 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -500, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            20
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                particleColorTexture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/color-bloodfade32.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.409994662 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.835294127, 0.301960796, 0.980392158, 1 }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.25
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Droplets_Erode.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Droplets.dds"
                numFrames: u16 = 4
                startFrame: u16 = 1
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.25
                }
                emitterLinger: option[f32] = {}
                emitterName: string = "flat1"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.700007617 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.23137255, 0.101960786, 0.250980407, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec4] = {
                            { 0.23137255, 0.101960786, 0.250980407, 0 }
                            { 0.23137255, 0.101960786, 0.250980407, 1 }
                            { 0.23137255, 0.101960786, 0.250980407, 0 }
                        }
                    }
                }
                pass: i16 = -1
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 270, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 420, 420 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 0, 0 }
                            { 0.949999988, 0.349999994, 0.349999994 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/Aura_Self.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.25
                }
                emitterLinger: option[f32] = {}
                emitterName: string = "flat2"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.409994662 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.929411769, 0.388235301, 1, 1 }
                }
                pass: i16 = 80
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 420, 420 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 0, 0 }
                            { 0.349999994, 0.349999994, 0.349999994 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Eye_Glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.75
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    0.150000006
                }
                isSingleParticle: flag = true
                emitterName: string = "blood_5"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 400, 600 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 600, 400, 600 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -900, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -900, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                particleColorTexture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/color-bloodfade32.dds"
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.36470589, 0.498039216, 0.600000024, 1 }
                }
                colorLookUpTypeY: u8 = 3
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 160, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Glass_Shards_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    4
                }
                isSingleParticle: flag = true
                emitterName: string = "Smoke"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 40, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 40, 20 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 2, 6 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 300, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 40, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            1
                            0
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.960006118, 0.209994659, 0.800000012, 0.190005347 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.960006118, 0.209994659, 0.800000012, 0.190005347 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/alphaslice_mesh.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 1, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 1, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 90, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 40, 40 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.25, 1, 1 }
                            { 1, 2, 2 }
                            { 1.5, 3, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/Sion_Skin05_Sl_Dust_01.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Gradients_Blur.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                    }
                    PaletteUAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 4
                    }
                    PaletteVAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                1
                                4
                            }
                        }
                    }
                    paletteCount: i32 = 4
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.25
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.150000006
                }
                isSingleParticle: flag = true
                emitterName: string = "blood_6"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 4, 0.5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.880003035 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.313725501, 0.980392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.313725501, 0.980392158, 0 }
                            { 1, 0.313725501, 0.980392158, 1 }
                            { 1, 0.313725501, 0.980392158, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 360, 0 }
                        }
                    }
                }
                directionVelocityScale: f32 = 0.00600000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 8, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.449999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 40, 48, 15 }
                            { 40, 8, 15 }
                            { 40, 8, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 2, 3, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/Dr_Mundo_Base_E_BuffDrips.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 1900, 200 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 1900, 200 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 6, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1200, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_CannisterModel02.scb"
                    }
                }
                blendMode: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 40
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 40, 40 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.275565594
                            0.529411793
                            0.574660659
                            0.683257937
                            0.837104082
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1, 1, 1 }
                            { 0.84690547, 0.84690547, 0.988235295 }
                            { 0.817179084, 0.817179084, 0.717647076 }
                            { 0.736917734, 0.736917734, 0.405882359 }
                            { 0.395955831, 0.395955831, 0.158823535 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/DrMundo_Base_Weapon_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 800, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 800, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -980, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -980, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_CannisterModel01.scb"
                    }
                }
                blendMode: u8 = 3
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.866666675, 0.866666675, 0.866666675, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 40
                isUniformScale: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 40, 40 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.275565594
                            0.529411793
                            0.574660659
                            0.683257937
                            0.837104082
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1, 1, 1 }
                            { 0.84690547, 0.84690547, 0.988235295 }
                            { 0.817179084, 0.817179084, 0.717647076 }
                            { 0.736917734, 0.736917734, 0.405882359 }
                            { 0.395955831, 0.395955831, 0.158823535 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/DrMundo_Base_Weapon_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                lifetime: option[f32] = {
                    12
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Ray"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.439993888 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.439993888 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.980392158, 0.698039234, 0.980392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.980392158, 0.698039234, 0.980392158, 0 }
                            { 0.980392158, 0.698039234, 0.980392158, 1 }
                            { 0.980392158, 0.698039234, 0.980392158, 1 }
                            { 0.980392158, 0.698039234, 0.980392158, 0 }
                        }
                    }
                }
                pass: i16 = 45
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.25
                                1
                            }
                            values: list[f32] = {
                                -2
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.25
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                miscRenderFlags: u8 = 1
                uvScrollAlphaMult: flag = false
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 500, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 500, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 0.75, 0.75 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.1875, 0.337499976, 0.75 }
                            { 0.375, 0.899999976, 0.75 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_Trail.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                            { 0.100000001, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 1 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Cas_Ground_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                texAddressModeMult: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.25
                }
                emitterLinger: option[f32] = {}
                emitterName: string = "flat3"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.129411772, 0.0627451017, 0.254901975, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec4] = {
                            { 0.129411772, 0.0627451017, 0.254901975, 0 }
                            { 0.129411772, 0.0627451017, 0.254901975, 1 }
                            { 0.129411772, 0.0627451017, 0.254901975, 0 }
                        }
                    }
                }
                pass: i16 = -1
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 420, 420 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.401493222
                            0.778280556
                            0.923076928
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 0.188235268, 0, 0 }
                            { 0.515294135, 0, 0 }
                            { 0.832941234, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/Aura_Self.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 150
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.75
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    0.0500000007
                }
                emitterName: string = "blood_8"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -500, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            1
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                    1
                                }
                                values: list[f32] = {
                                    0
                                    129600
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/color-bloodfade32.dds"
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.36470589, 0.498039216, 0.600000024, 1 }
                }
                colorLookUpTypeY: u8 = 3
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 160, 100, 100 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Glass_Shards_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    0.150000006
                }
                isSingleParticle: flag = true
                emitterName: string = "blood_9"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 200, 500 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 500, 200, 500 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -500, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            20
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                particleColorTexture: string = "ASSETS/Characters/Darius/Skins/Base/Particles/color-bloodfade32.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.280003041 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.58431375, 0.80392158, 0.823529422, 1 }
                }
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Glass_Shards_2x2.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "DrMundo_Base_P_Cannister_Crush"
        particlePath: string = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Crush"
        soundOnCreateDefault: string = "Play_sfx_DrMundo_DrMundoPObject_break"
        flags: u8 = 198
    }
    "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Ground" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.289997697, 0.779995441, 0.990005314 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.235294119, 0.13333334, 0.388235301, 1 }
                            { 0.23137255, 0.137254909, 0.290196091, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 200, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, -100 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Ziggs/Skins/Base/Particles/Ziggs_Base_R_SoftCircle.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.149019614, 0.0745098069, 0.188235298, 0.772549033 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.235294119, 0.13333334, 0.388235301, 1 }
                            { 0.23137255, 0.137254909, 0.290196091, 0 }
                        }
                    }
                }
                pass: i16 = -20
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, -100 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Ziggs/Skins/Base/Particles/Ziggs_Base_R_SoftCircle.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    6
                }
                emitterName: string = "Shapes"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 40, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 100 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 100 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[f32] = {
                            0
                            0
                            0
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.719996929, 0.379995435, 0.960006118, 0.549996197 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.549019635, 0.882352948, 1, 0.505882382 }
                            { 0.75686276, 0.545098066, 1, 1 }
                            { 0.784313738, 0.345098048, 1, 0.498039216 }
                            { 0.419607848, 0.0823529437, 1, 0 }
                        }
                    }
                }
                pass: i16 = 600
                alphaRef: u8 = 130
                softParticleParams: pointer = VfxSoftParticleDefinitionData {}
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.50999999
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    4
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 80, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.900000036, 0.5, 1 }
                            { 0.75, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/Illaoi_Base_E_IdolShapes.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    6
                }
                emitterName: string = "Shapes1"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 40, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 80, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 80, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 0, 100 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 0, 100 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[f32] = {
                            0
                            0
                            0
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.835294187, 0.835294187, 0.835294187, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.549996197, 0.880003035, 1, 0 }
                            { 0.458823532, 0.929411769, 1, 1 }
                            { 0.345098048, 0.913725495, 1, 1 }
                            { 0.419607848, 0.0823529437, 1, 0 }
                        }
                    }
                }
                pass: i16 = 600
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_R_Bubble_Erode.dds"
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.50999999
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 80, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.5
                            0.772540033
                            0.851258576
                            0.897025168
                            0.935926795
                            0.980000019
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.25, 0, 0 }
                            { 0.75, 1, 1 }
                            { 1.13157892, 0, 0 }
                            { 0.934210539, 0, 0 }
                            { 1.01315784, 0, 0 }
                            { 0.881578922, 0, 0 }
                            { 0.850000024, 0, 0 }
                            { 1.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_GroundGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.530006886 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0980392173, 0.733333349, 0.713725507, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.0980392173, 0.733333349, 0.713725507, 0 }
                            { 0.0311418679, 0.704575181, 0.618562102, 1 }
                            { 0.0215301812, 0.63843137, 0.46742022, 1 }
                            { 0.00538254529, 0.00287581724, 0.0671741664, 0 }
                        }
                    }
                }
                pass: i16 = -10
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.75, 0, 0 }
                            { 0.75, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Backdrop.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    6
                }
                emitterName: string = "Temp_GroundGlow1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 0, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 0, 30 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 0, 30 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.549996197 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.541176498, 0.329411775, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.340000004
                            1
                        }
                        values: list[vec4] = {
                            { 0.541176498, 0.329411775, 1, 0 }
                            { 0.233448669, 0.112387545, 0.945098042, 1 }
                            { 0.0297116488, 0.00129181088, 0.0941176489, 0 }
                        }
                    }
                }
                pass: i16 = -2
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 270, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 10, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.637500048, 0, 0 }
                            { 0.75, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Backdrop.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Ripple_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.669993162 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.180392161, 0.764705896, 0.647058845, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.180392161, 0.764705896, 0.647058845, 0 }
                            { 0.180392161, 0.764705896, 0.647058845, 1 }
                            { 0.180392161, 0.764705896, 0.647058845, 1 }
                            { 0.0141484048, 0.188927338, 0.124336801, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.949999988
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.129999995
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Chemical_Mult.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Gradients_Blur.dds"
                    PaletteTextureAddressMode: u8 = 0
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 0, 1 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                    }
                    PaletteUAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                2
                            }
                        }
                    }
                    PaletteVAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 2
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                2
                                2
                            }
                        }
                    }
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.200000003 }
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    6.5
                }
                emitterName: string = "Temp_Mesh1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Ripple_Mesh.scb"
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.379995435 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.498039216, 0.850980401, 0.905882359, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.320588231
                            0.514705896
                            0.70588237
                            1
                        }
                        values: list[vec4] = {
                            { 0.498039216, 0.850980401, 0.905882359, 0 }
                            { 0.498039216, 0.850980401, 0.905882359, 1 }
                            { 0.397492468, 0.710615873, 0.745566845, 0.327868849 }
                            { 0.295083731, 0.567651927, 0.582282484, 0.639344275 }
                            { 0.194226667, 0.426854223, 0.421472102, 0.180327863 }
                            { 0.0390619002, 0.210242212, 0.174071521, 0 }
                        }
                    }
                }
                pass: i16 = 8
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.850000024
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.340000004
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_W_LightningErosion03.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Lightning03.dds"
                frameRate: f32 = 5
                numFrames: u16 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.200000003 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
                texDiv: vec2 = { 2, 1 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.50999999
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 2, 1 }
                        }
                    }
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh3"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_PuddleMesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.530006886 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.529411793, 0.286274523, 0.827450991, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.529411793, 0.286274523, 0.827450991, 0 }
                            { 0.529411793, 0.286274523, 0.827450991, 1 }
                            { 0.529411793, 0.286274523, 0.827450991, 1 }
                            { 0.0415224917, 0.0707266405, 0.159000382, 0 }
                        }
                    }
                }
                pass: i16 = -4
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                0.949999988
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.129999995
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "alpha puddle"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_PuddleMesh.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.478431374, 0.239215687, 0.615686297, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.478431374, 0.239215687, 0.615686297, 0 }
                            { 0.478431374, 0.239215687, 0.615686297, 1 }
                            { 0.478431374, 0.239215687, 0.615686297, 1 }
                            { 0.0375240296, 0.0591003448, 0.118308343, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                0.949999988
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.129999995
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh5"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubblemesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.439993888 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.53725493, 0.403921574, 0.866666675, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.53725493, 0.403921574, 0.866666675, 0 }
                            { 0.53725493, 0.403921574, 0.866666675, 1 }
                            { 0.53725493, 0.403921574, 0.866666675, 1 }
                            { 0.0421376415, 0.0997923911, 0.166535944, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.25
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.340000004
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble_Mesh_Erode.dds"
                }
                disableBackfaceCull: bool = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.649999976, 1, 0.649999976 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.449526817
                            0.602193058
                            0.680911601
                            0.726678193
                            0.787661791
                            0.854889572
                            0.980000019
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.324999988, 1, 0.324999988 }
                            { 0.496052623, 1.01315784, 0.495950013 }
                            { 0.752631545, 1.15799999, 0.752699971 }
                            { 0.624342144, 0.961000025, 0.624650002 }
                            { 0.675657868, 1.03900003, 0.67535001 }
                            { 0.538815796, 0.828999996, 0.538850009 }
                            { 0.667105258, 1.02600002, 0.666900039 }
                            { 0.55250001, 2, 0.55250001 }
                            { 0.324999988, 0, 0.324999988 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubble_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.850000024
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    6.5
                }
                emitterName: string = "Temp_Mesh6"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 80, 0, 80 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 80, 0, 80 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubblemesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.570000768 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.570000768 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.380392164, 0.34117648, 0.90196079, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.380392164, 0.34117648, 0.90196079, 0 }
                            { 0.380392164, 0.34117648, 0.90196079, 1 }
                            { 0.380392164, 0.34117648, 0.90196079, 1 }
                            { 0.0298346803, 0.0842906609, 0.173317954, 0 }
                        }
                    }
                }
                pass: i16 = 48
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.25
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.340000004
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble_Mesh_Erode.dds"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 5, 1 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.449526817
                            0.602193058
                            0.680911601
                            0.726678193
                            0.787661791
                            0.854889572
                            0.980000019
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.1875, 0, 0 }
                            { 0.572368443, 1.01315784, 1.01315784 }
                            { 0.868421078, 0, 0 }
                            { 0.720394731, 0, 0 }
                            { 0.779605269, 0, 0 }
                            { 0.621710539, 0, 0 }
                            { 0.769736886, 0, 0 }
                            { 0.637500048, 0, 0 }
                            { 1.125, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubble_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    6.5
                }
                emitterName: string = "Temp_Mesh7"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 80, 0, 80 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 80, 0, 80 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubblemesh.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.540001512 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0.435294122, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.549019635, 0.435294122, 1, 0 }
                            { 0.549019635, 0.435294122, 1, 1 }
                            { 0.549019635, 0.435294122, 1, 1 }
                            { 0.0430603623, 0.107543252, 0.192156866, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.25
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.340000004
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble_Mesh_Erode.dds"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 5, 1 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.449526817
                            0.602193058
                            0.680911601
                            0.726678193
                            0.787661791
                            0.854889572
                            0.980000019
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.1875, 0, 0 }
                            { 0.572368443, 1.01315784, 1.01315784 }
                            { 0.868421078, 0, 0 }
                            { 0.720394731, 0, 0 }
                            { 0.779605269, 0, 0 }
                            { 0.621710539, 0, 0 }
                            { 0.769736886, 0, 0 }
                            { 0.637500048, 0, 0 }
                            { 1.125, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Bubble_Mask.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Ray"
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.97999543 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.34117648, 0.227450982, 0.43921569, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.34117648, 0.227450982, 0.43921569, 0 }
                            { 0.34117648, 0.227450982, 0.43921569, 1 }
                            { 0.34117648, 0.227450982, 0.43921569, 0 }
                        }
                    }
                }
                uvScrollClampMult: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 50 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 0.75, 0.75 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.75, 0.75, 0.75 }
                            { 0.75, 1.125, 0.75 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Smokey_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_P_Ray_Mult.dds"
                texAddressModeMult: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh8"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Funnel_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.90196079, 0.549019635, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.90196079, 0.549019635, 1, 0 }
                            { 0.90196079, 0.549019635, 1, 1 }
                            { 0.90196079, 0.549019635, 1, 1 }
                            { 0.16978085, 0.103344873, 0.188235298, 0 }
                        }
                    }
                }
                pass: i16 = 20
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 9, 3, 9 }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Chemical_Mult.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.649999976 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.25
                }
                lifetime: option[f32] = {
                    2
                }
                emitterName: string = "Temp_Ray1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -20, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 125, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 125, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.340001523 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.340001523 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.635294139, 0.321568638, 0.992156863, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.635294139, 0.321568638, 0.992156863, 0 }
                            { 0.635294139, 0.321568638, 0.992156863, 1 }
                            { 0.0921799317, 0.0302652828, 0.303483278, 0.56078434 }
                            { 0.191833913, 0.0971011147, 0.299592465, 0 }
                        }
                    }
                }
                pass: i16 = 45
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_Ground_Trail_Erode.dds"
                }
                miscRenderFlags: u8 = 1
                uvScrollAlphaMult: flag = false
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 300, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 300, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 0.75, 0.75 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.75, 0.337499976, 0.75 }
                            { 0.375, 0.75, 0.75 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 1 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Cas_Ground_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                texAddressModeMult: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                isSingleParticle: flag = true
                emitterName: string = "Beaker4"
                Linger: pointer = VfxLingerDefinitionData {
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.941176474, 0.941176474, 0.941176474, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skl"
                        mAnimationName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_CanisterIdle.anm"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Ziggs/Skins/Skin01/Particles/color-hold.DDS"
                blendMode: u8 = 3
                pass: i16 = 20
                censorModulateValue: vec4 = { 0.909803927, 0.925490201, 0.905882359, 1 }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.647058845, 0.243137255, 1, 1 }
                    fresnel: f32 = 0.5
                    fresnelColor: vec4 = { 0.211764708, 0.0549019612, 0.337254912, 0 }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -12 }
                            { 0, 0, -12 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 1.29999995, 1.29999995 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/DrMundo_Base_Weapon_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                isSingleParticle: flag = true
                emitterName: string = "Beaker5"
                Linger: pointer = VfxLingerDefinitionData {
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.941176474, 0.941176474, 0.941176474, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Capacitor_Rigged.skl"
                        mAnimationName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_CanisterIdle.anm"
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Ziggs/Skins/Skin01/Particles/color-hold.DDS"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.129999995
                            0.349999994
                            0.649999976
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.984313726, 0.43921569, 1 }
                            { 0.423529416, 0.266666681, 0.105882354, 0 }
                            { 1, 0.972549021, 0.152941182, 1 }
                            { 0.349019617, 0.258823544, 0.117647059, 0 }
                            { 1, 0.905882359, 0.180392161, 1 }
                            { 0.196078435, 0.0941176489, 0.0235294122, 0 }
                        }
                    }
                }
                pass: i16 = 25
                censorModulateValue: vec4 = { 0.909803927, 0.925490201, 0.905882359, 1 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -12 }
                            { 0, 0, -12 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/3161color-hold.TFT_Booms_Set7_5.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh9"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Ripple_Mesh.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.650003791 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.58431375, 0.23137255, 0.607843161, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.58431375, 0.23137255, 0.607843161, 0 }
                            { 0.58431375, 0.23137255, 0.607843161, 1 }
                            { 0.58431375, 0.23137255, 0.607843161, 0.519996941 }
                            { 0.0458285324, 0.0571626313, 0.11680124, 0 }
                        }
                    }
                }
                pass: i16 = -2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.949999988
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.129999995
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0199999996
                            0.0799999982
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.99000001, 0, 0 }
                            { 0.899999976, 1, 1 }
                            { 0.899999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Chemical_Mult.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Gradients_Blur.dds"
                    PaletteTextureAddressMode: u8 = 0
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 0, 0.540001512 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                    }
                    PaletteUAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 2
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                2
                            }
                        }
                    }
                    PaletteVAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 0.5
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 2 }
                }
                textureMult: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Puddle_Mask.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh10"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -40, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Funnel_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.596078455, 0.164705887, 0.737254918, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.596078455, 0.164705887, 0.737254918, 0 }
                            { 0.596078455, 0.164705887, 0.737254918, 1 }
                            { 0.596078455, 0.164705887, 0.737254918, 1 }
                            { 0.112203002, 0.0310034603, 0.13877739, 0 }
                        }
                    }
                }
                pass: i16 = 40
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Bubble_Mesh_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 6, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0, 0.300000012 }
                            { 1, 2, 1 }
                            { 2, 0, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Goop.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, -1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh12"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_R_Funnel_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.439993888 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.474509805, 0.164705887, 0.529411793, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.474509805, 0.164705887, 0.529411793, 0 }
                            { 0.474509805, 0.164705887, 0.529411793, 1 }
                            { 0.474509805, 0.164705887, 0.529411793, 1 }
                            { 0.0893194973, 0.0310034603, 0.0996539816, 0 }
                        }
                    }
                }
                pass: i16 = -20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.850000024
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                                2
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.25
                    erosionMapName: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Erode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 9, 0, 9 }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_P_Puddle_Goop.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.400000006 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh13"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/sphere.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/checkers.dds"
            }
        }
        particleName: string = "DrMundo_Base_P_Cannister_Ground"
        particlePath: string = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Ground"
        soundPersistentDefault: string = "Play_sfx_DrMundo_DrMundoPObject_land"
        flags: u8 = 212
    }
    "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_ChildTrail" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "BloodBitsAdd"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 3, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, -50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, -50, 50 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 2, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -400, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -400, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 30, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 30, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0.282352954, 0.670588255, 0.4627451, 1 }
                            { 0.101960786, 0.670588255, 0.482352942, 0.749019623 }
                            { 0, 0.392156869, 0.160784319, 0 }
                        }
                    }
                }
                pass: i16 = 18
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 30 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.699999988, 0.699999988, 0.699999988 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Mote.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "BloodBitsBlend"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 3, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, -50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, -50, 50 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 2, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -300, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 30, 30, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 30, 30, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.564705908, 0.874509811, 0.737254918, 0 }
                            { 0.380392164, 0.874509811, 0.670588255, 1 }
                            { 0.0274509806, 0.294117659, 0.113725491, 0.749019623 }
                            { 0.239215687, 0.266666681, 0, 0 }
                        }
                    }
                }
                pass: i16 = 18
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 30 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.699999988, 0.699999988, 0.699999988 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Mote.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.300000012
                            0.075000003
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "Front"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 1 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 300
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 300, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.286274999, 0.0745100006, 0.164706007, 1 }
                            { 0.286274999, 0.0745100006, 0.164706007, 0.69799298 }
                            { 0.286274999, 0.0745100006, 0.164706007, 0.297993004 }
                            { 0.286274999, 0.0745100006, 0.164706007, 0 }
                        }
                    }
                }
                pass: i16 = 8
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 25, 25 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 25, 25, 25 }
                            { 25, 25, 25 }
                            { 25, 25, 25 }
                            { 2.5, 25, 25 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_Mis_Front.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0.300000012
                            0.075000003
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "FrontAdd"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 30, 1 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 300
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 300, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0.0156859998, 0.497992992 }
                            { 1, 0, 0.0156859998, 0.349004 }
                            { 1, 0, 0.0156859998, 0.149003997 }
                            { 1, 0, 0.0156859998, 0 }
                        }
                    }
                }
                pass: i16 = 8
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 25, 25 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 25, 25, 25 }
                            { 25, 25, 25 }
                            { 25, 25, 25 }
                            { 2.5, 25, 25 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_Mis_Front.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Glow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 10, 10 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -300, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 2500
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 300, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.130006865, 0.680003047, 0.349996179, 0.250003815 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.130006865, 0.680003047, 0.349996179, 0 }
                            { 0.130006865, 0.680003047, 0.349996179, 0.250003815 }
                            { 0.130006865, 0.680003047, 0.349996179, 0.250003815 }
                            { 0.130006865, 0.680003047, 0.349996179, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.53725493, 0.831372559, 0.749019623, 0 }
                            { 0.200000003, 0.564705908, 0.58431375, 0.800000012 }
                            { 0.125490203, 0.670588255, 0.282352954, 0.250980407 }
                            { 0.223529413, 0.274509817, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 90, 90, 90 }
                            { 90, 90, 90 }
                            { 90, 90, 90 }
                            { 9, 90, 90 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_mis_01_Ribbon.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "RibbonAdd"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0.400000006 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.56078434, 0.41568628, 0.345098048, 0 }
                            { 0.815686285, 0.239215687, 0.160784319, 0.827450991 }
                            { 1, 0, 0, 0.525490224 }
                            { 0.690196097, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 22
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.699999988
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_mis_01_Ribbon.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "RibbonBlend"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -500, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 50 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.549996197 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.549996197 }
                            { 1, 1, 1, 0.549996197 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.56078434, 0.41568628, 0.345098048, 0 }
                            { 0.815686285, 0.239215687, 0.160784319, 0.827450991 }
                            { 1, 0, 0, 0.525490224 }
                            { 0.690196097, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 21
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.699999988
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_mis_01_Ribbon.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Trail"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -720, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -720, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 600, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.289997697 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.289997697 }
                            { 1, 1, 1, 0.289997697 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.890196085, 0.70588237, 0 }
                            { 1, 0.592156887, 0.388235301, 1 }
                            { 0.843137264, 0.117647059, 0.0941176489, 0.56078434 }
                            { 0.239215687, 0, 0, 0.180392161 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 7
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 60, 60 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.20000005, 1.20000005, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_Tar_Trail.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.400000006, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.400000006, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "RibbonBlend1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -500, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 20 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.200000003 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.200000003 }
                            { 1, 1, 1, 0.200000003 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.56078434, 0.184313729, 0, 0 }
                            { 0.588235319, 0, 0, 0.827450991 }
                            { 0.690196097, 0, 0.184313729, 0.525490224 }
                            { 0.690196097, 0.176470593, 0.176470593, 0 }
                        }
                    }
                }
                pass: i16 = 21
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 10, 10 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.699999988
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/DrMundo_Base_Q_mis_01_Ribbon.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "RibbonAdd1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 50, 50 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 120, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.87843138, 0.505882382, 0 }
                            { 0.65882355, 1, 0.290196091, 0.827450991 }
                            { 0.117647059, 0.905882359, 0.34117648, 0.525490224 }
                            { 0.0313725509, 0.690196097, 0.56078434, 0 }
                        }
                    }
                }
                pass: i16 = 30
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.699999988
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/DrMundo/Skins/Base/Particles/global_SS_cas_01_vortex_alpha.SRI_Slots.dds"
            }
        }
        particleName: string = "DrMundo_Base_Q_ChildTrail"
        particlePath: string = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_ChildTrail"
    }
    "Characters/DrMundo/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "DrMundo_BA_tar_01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_BA_tar_01"
            "DrMundo_BA_tar_crit_01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_BA_tar_crit_01"
            "DrMundo_E_cas_01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_cas_01"
            "DrMundo_Q_mis_01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_mis_01"
            "DrMundo_Q_tar_01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_tar_01"
            "DrMundo_R_cas_01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_R_cas_01"
            "DrMundo_R_cas_02" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_R_cas_02"
            0x7e8fc272 = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_R_Buf"
            "DrMundo_R_tar_hit_01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_R_tar_hit_01"
            "DrMundo_W_cas_01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_W_cas_01"
            0x071ca4eb = "Characters/DrMundo/Skins/Skin0/Particles/Global_Slow"
            "DrMundo_Q_Mis01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_mis_01"
            0x99ad9780 = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_W_ChildFireball"
            "DrMundo_Q_ChildTrail" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_ChildTrail"
            "DrMundo_Q_Tar_Cleaver" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_Tar_Cleaver"
            "DrMundo_Q_Tar_Cleaver_Killed" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_Tar_Cleaver_Killed"
            "DrMundo_W_Tar" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_W_Tar"
            "DrMundo_Base_BA_Swipe_1" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_BA_Swipe_1"
            "DrMundo_Base_BA_Swipe_2" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_BA_Swipe_2"
            "DrMundo_E_weapon_01" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_weapon_01"
            "DrMundo_P_Cannister_Crush" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Crush"
            0x5da3f2b5 = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_W_2"
            "DrMundo_E_Tar" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_Tar"
            "DrMundo_P_Block_Spell_cas" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Block_Spell_cas"
            "DrMundo_P_Buf_Regen" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Buf_Regen"
            "DrMundo_P_Capacitor" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Capacitor"
            "DrMundo_P_Capacitor_Glow" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Capacitor_Glow"
            "DrMundo_P_ChunkLandIndicator" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_ChunkLandIndicator"
            "DrMundo_P_Cannister_Missile" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Missile"
            "DrMundo_E_Circular_Warning" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_Circular_Warning"
            "DrMundo_E_Circular_Warning_Main" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_Circular_Warning_Main"
            "DrMundo_E_Beam" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_Beam"
            "DrMundo_P_Cannister_Ground" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Ground"
            "DrMundo_P_TrackerLine" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_TrackerLine"
            "DrMundo_R_EyeGlow_L" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_R_EyeGlow_L"
            "DrMundo_R_EyeGlow_R" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Emote_EyeGlow_R"
            "DrMundo_Q_Bonesaw_Child" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_Bonesaw_Child"
            "DrMundo_R_Haste" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_R_Haste"
            "DrMundo_W_Cas_Head_Shock" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_W_Cas_Head_Shock"
            "DrMundo_W_Sparks_Child" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_W_Sparks_Child"
            0xc6bdd038 = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_Knockback_Wave"
            "DrMundo_E_Buf" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_Buf"
            "DrMundo_E_Dirt_Child" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_Dirt_Child"
            "DrMundo_P_Cannister_Trail_child" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Trail_child"
            "DrMundo_E_Knockback_Tar" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_Knockback_Tar"
            "DrMundo_P_Heal" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Heal"
            "DrMundo_P_Body_Fresnel" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Body_Fresnel"
            "DrMundo_P_Cannister_UltForm" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_UltForm"
            "DrMundo_P_Cannister_Ground_Enemy" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Ground_Enemy"
            "DrMundo_P_ChunkLandIndicator_Enemy" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_ChunkLandIndicator_Enemy"
            "DrMundo_BA_2_Spit" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_BA_2_Spit"
            "DrMundo_BA_Crit_Swipe" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_BA_Crit_Swipe"
            "DrMundo_BA_tar_02" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_BA_tar_02"
            "DrMundo_BA_Turret_Hit" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_BA_Turret_Hit"
            "DrMundo_W_2_Tar" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_W_2_Tar"
            "DrMundo_R_Ground_Puddle_Child" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_R_Ground_Puddle_Child"
            "DrMundo_R_Buckle_Trail_Child" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_R_Buckle_Trail_Child"
            "DrMundo_Q_Puddle_Child" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Q_Puddle_Child"
            "DrMundo_P_Cannister_Into_Ult_Transition" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Into_Ult_Transition"
            "DrMundo_P_Cannister_Outof_Ult_Transition" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cannister_Outof_Ult_Transition"
            "DrMundo_E_Swipe" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_E_Swipe"
            "DrMundo_Emote_Death_Dirt" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Emote_Death_Dirt"
            "DrMundo_Emote_Winddown_Dirt" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Emote_Winddown_Dirt"
            "DrMundo_Emote_Recall_Beaker_Break" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Emote_Recall_Beaker_Break"
            "DrMundo_Emote_Recall_Liquid" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Emote_Recall_Liquid"
            "DrMundo_Recall_Drips" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Recall_Drips"
            "DrMundo_Emote_Recall_Eye_Glow" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Emote_Recall_Eye_Glow"
            "DrMundo_Emote_Recall_Launch" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Emote_Recall_Launch"
            "DrMundo_Emote_Joke_Spit" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_Emote_Joke_Spit"
            "DrMundo_P_Cash_Sign_Shoulder_R" = "Characters/DrMundo/Skins/Skin0/Particles/DrMundo_Base_P_Cash_Sign_Shoulder_R"
        }
    }
}
