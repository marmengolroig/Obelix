import sys
sys.path.append("..")
import geopandas as gpd
import os
import folium
import pymap3d as pm

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import QWebEngineView

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

from decoder import decode

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                if not MainWindow.objectName():
                        MainWindow.setObjectName(u"MainWindow")
                        MainWindow.resize(990, 588)
                        MainWindow.setStyleSheet(u"* {\n"
                "	border: none;\n"
                "	background-color: transparent;\n"
                "	background: transparent;\n"
                "	padding: 0;\n"
                "	margin: 0;\n"
                "	color: #fff;\n"
                "}\n"
                "\n"
                "#centralwidget {\n"
                "	background-color: #1f232a;\n"
                "}\n"
                "#leftMenuSubcontainer, #rightMenuSubContainer{\n"
                "	background-color: #16191d;\n"
                "}\n"
                "\n"
                "#leftMenuSubcontainer QPushButton { \n"
                "	text-align: left; \n"
                "	padding: 5px 10px;\n"
                "	border-top-left-radius: 10px;\n"
                "	border-bottom-left-radius: 10px;\n"
                "}\n"
                "\n"
                "#centerMenuSubContainer, #rightMenuSubContainer{\n"
                "	background-color: #2c313c;\n"
                "}\n"
                "\n"
                "#frame_4, #frame_8, #popupNotificationSubContainer{\n"
                "	background-color: #16191d;\n"
                "	border-radius: 10px;\n"
                "}\n"
                "#headerContainer, #footerContainer{\n"
                "	background-color: #2c313c;\n"
                "\n"
                "}\n"
                "")
                self.centralwidget = QWidget(MainWindow)
                self.centralwidget.setObjectName(u"centralwidget")
                self.horizontalLayout = QHBoxLayout(self.centralwidget)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName(u"horizontalLayout")
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
                self.leftMenuContainer.setObjectName(u"leftMenuContainer")
                self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
                self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName(u"verticalLayout")
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.leftMenuSubcontainer = QWidget(self.leftMenuContainer)
                self.leftMenuSubcontainer.setObjectName(u"leftMenuSubcontainer")
                self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubcontainer)
                self.verticalLayout_2.setSpacing(0)
                self.verticalLayout_2.setObjectName(u"verticalLayout_2")
                self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
                self.frame = QFrame(self.leftMenuSubcontainer)
                self.frame.setObjectName(u"frame")
                self.frame.setStyleSheet(u"color: #fff")
                self.frame.setFrameShape(QFrame.StyledPanel)
                self.frame.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_2 = QHBoxLayout(self.frame)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.menuBtn = QPushButton(self.frame)
                self.menuBtn.setObjectName(u"menuBtn")
                self.menuBtn.setStyleSheet(u"color: #fff;""")
                icon = QIcon()
                icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.menuBtn.setIcon(icon)
                self.menuBtn.setIconSize(QSize(24, 24))

                self.horizontalLayout_2.addWidget(self.menuBtn)


                self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

                self.frame_2 = QFrame(self.leftMenuSubcontainer)
                self.frame_2.setObjectName(u"frame_2")
                sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
                self.frame_2.setSizePolicy(sizePolicy)
                self.frame_2.setFrameShape(QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QFrame.Raised)
                self.verticalLayout_3 = QVBoxLayout(self.frame_2)
                self.verticalLayout_3.setSpacing(0)
                self.verticalLayout_3.setObjectName(u"verticalLayout_3")
                self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
                self.homeBtn = QPushButton(self.frame_2)
                self.homeBtn.setObjectName(u"homeBtn")
                self.homeBtn.setStyleSheet(u"background-color: #1f232a;""color: #fff;")
                icon1 = QIcon()
                icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.homeBtn.setIcon(icon1)
                self.homeBtn.setIconSize(QSize(24, 24))

                self.verticalLayout_3.addWidget(self.homeBtn)

                self.mapBtn = QPushButton(self.frame_2)
                self.mapBtn.setObjectName(u"mapBtn")
                icon2 = QIcon()
                icon2.addFile(u":/icons/icons/map.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.mapBtn.setIcon(icon2)
                self.mapBtn.setIconSize(QSize(24, 24))

                self.verticalLayout_3.addWidget(self.mapBtn)

                self.reportBtn = QPushButton(self.frame_2)
                self.reportBtn.setObjectName(u"reportBtn")
                icon3 = QIcon()
                icon3.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.reportBtn.setIcon(icon3)
                self.reportBtn.setIconSize(QSize(24, 24))

                self.verticalLayout_3.addWidget(self.reportBtn)


                self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

                self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

                self.verticalLayout_2.addItem(self.verticalSpacer)

                self.frame_3 = QFrame(self.leftMenuSubcontainer)
                self.frame_3.setObjectName(u"frame_3")
                self.frame_3.setFrameShape(QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QFrame.Raised)
                self.verticalLayout_4 = QVBoxLayout(self.frame_3)
                self.verticalLayout_4.setSpacing(0)
                self.verticalLayout_4.setObjectName(u"verticalLayout_4")
                self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
                self.settingsBtn = QPushButton(self.frame_3)
                self.settingsBtn.setObjectName(u"settingsBtn")
                icon4 = QIcon()
                icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.settingsBtn.setIcon(icon4)
                self.settingsBtn.setIconSize(QSize(24, 24))

                self.verticalLayout_4.addWidget(self.settingsBtn)

                self.infoBtn = QPushButton(self.frame_3)
                self.infoBtn.setObjectName(u"infoBtn")
                icon5 = QIcon()
                icon5.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.infoBtn.setIcon(icon5)
                self.infoBtn.setIconSize(QSize(24, 24))

                self.verticalLayout_4.addWidget(self.infoBtn)

                self.helpBtn = QPushButton(self.frame_3)
                self.helpBtn.setObjectName(u"helpBtn")
                icon6 = QIcon()
                icon6.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.helpBtn.setIcon(icon6)
                self.helpBtn.setIconSize(QSize(24, 24))

                self.verticalLayout_4.addWidget(self.helpBtn)


                self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


                self.verticalLayout.addWidget(self.leftMenuSubcontainer)


                self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

                self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
                self.centerMenuContainer.setObjectName(u"centerMenuContainer")
                self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
                self.verticalLayout_5.setSpacing(0)
                self.verticalLayout_5.setObjectName(u"verticalLayout_5")
                self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
                self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
                self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
                self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
                self.verticalLayout_6.setSpacing(5)
                self.verticalLayout_6.setObjectName(u"verticalLayout_6")
                self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
                self.frame_4 = QFrame(self.centerMenuSubContainer)
                self.frame_4.setObjectName(u"frame_4")
                self.frame_4.setFrameShape(QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
                self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
                self.label = QLabel(self.frame_4)
                self.label.setObjectName(u"label")
                self.label.setAlignment(Qt.AlignCenter)

                self.horizontalLayout_3.addWidget(self.label)

                self.closeCenterMenuBtn = QPushButton(self.frame_4)
                self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
                icon7 = QIcon()
                icon7.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.closeCenterMenuBtn.setIcon(icon7)
                self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

                self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


                self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

                self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
                self.centerMenuPages.setObjectName(u"centerMenuPages")
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.verticalLayout_7 = QVBoxLayout(self.page)
                self.verticalLayout_7.setObjectName(u"verticalLayout_7")
                self.label_2 = QLabel(self.page)
                self.label_2.setObjectName(u"label_2")
                font = QFont()
                font.setPointSize(13)
                self.label_2.setFont(font)
                self.label_2.setAlignment(Qt.AlignCenter)

                self.verticalLayout_7.addWidget(self.label_2)

                self.centerMenuPages.addWidget(self.page)
                self.page_2 = QWidget()
                self.page_2.setObjectName(u"page_2")
                self.verticalLayout_8 = QVBoxLayout(self.page_2)
                self.verticalLayout_8.setObjectName(u"verticalLayout_8")
                self.label_3 = QLabel(self.page_2)
                self.label_3.setObjectName(u"label_3")
                self.label_3.setFont(font)
                self.label_3.setAlignment(Qt.AlignCenter)

                self.verticalLayout_8.addWidget(self.label_3)

                self.centerMenuPages.addWidget(self.page_2)
                self.page_3 = QWidget()
                self.page_3.setObjectName(u"page_3")
                self.verticalLayout_9 = QVBoxLayout(self.page_3)
                self.verticalLayout_9.setObjectName(u"verticalLayout_9")
                self.label_4 = QLabel(self.page_3)
                self.label_4.setObjectName(u"label_4")
                self.label_4.setFont(font)
                self.label_4.setAlignment(Qt.AlignCenter)

                self.verticalLayout_9.addWidget(self.label_4)

                self.centerMenuPages.addWidget(self.page_3)

                self.verticalLayout_6.addWidget(self.centerMenuPages)


                self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


                self.horizontalLayout.addWidget(self.centerMenuContainer)

                self.mainBodyContainer = QWidget(self.centralwidget)
                self.mainBodyContainer.setObjectName(u"mainBodyContainer")
                sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)
                sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
                self.mainBodyContainer.setSizePolicy(sizePolicy1)
                self.mainBodyContainer.setStyleSheet(u"")
                self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
                self.verticalLayout_10.setSpacing(0)
                self.verticalLayout_10.setObjectName(u"verticalLayout_10")
                self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
                self.headerContainer = QWidget(self.mainBodyContainer)
                self.headerContainer.setObjectName(u"headerContainer")
                self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
                self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
                self.frame_5 = QFrame(self.headerContainer)
                self.frame_5.setObjectName(u"frame_5")
                self.frame_5.setFrameShape(QFrame.StyledPanel)
                self.frame_5.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
                self.horizontalLayout_7.setSpacing(6)
                self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
                self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
                self.label_5 = QLabel(self.frame_5)
                self.label_5.setObjectName(u"label_5")
                self.label_5.setMaximumSize(QSize(40, 40))
                self.label_5.setPixmap(QPixmap(u":/images/logo.png"))
                self.label_5.setScaledContents(True)

                self.horizontalLayout_7.addWidget(self.label_5)

                self.label_6 = QLabel(self.frame_5)
                self.label_6.setObjectName(u"label_6")
                font1 = QFont()
                font1.setPointSize(13)
                font1.setBold(True)
                font1.setWeight(75)
                self.label_6.setFont(font1)

                self.horizontalLayout_7.addWidget(self.label_6)


                self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

                self.frame_6 = QFrame(self.headerContainer)
                self.frame_6.setObjectName(u"frame_6")
                self.frame_6.setFrameShape(QFrame.StyledPanel)
                self.frame_6.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
                self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
                self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
                self.notificationBtn = QPushButton(self.frame_6)
                self.notificationBtn.setObjectName(u"notificationBtn")
                icon8 = QIcon()
                icon8.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.notificationBtn.setIcon(icon8)
                self.notificationBtn.setIconSize(QSize(24, 24))

                self.horizontalLayout_6.addWidget(self.notificationBtn)

                self.moreMenuBtn = QPushButton(self.frame_6)
                self.moreMenuBtn.setObjectName(u"moreMenuBtn")
                icon9 = QIcon()
                icon9.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.moreMenuBtn.setIcon(icon9)
                self.moreMenuBtn.setIconSize(QSize(24, 24))

                self.horizontalLayout_6.addWidget(self.moreMenuBtn)

                self.profileMenuBtn = QPushButton(self.frame_6)
                self.profileMenuBtn.setObjectName(u"profileMenuBtn")
                icon10 = QIcon()
                icon10.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.profileMenuBtn.setIcon(icon10)
                self.profileMenuBtn.setIconSize(QSize(24, 24))

                self.horizontalLayout_6.addWidget(self.profileMenuBtn)


                self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

                self.frame_7 = QFrame(self.headerContainer)
                self.frame_7.setObjectName(u"frame_7")
                self.frame_7.setFrameShape(QFrame.StyledPanel)
                self.frame_7.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
                self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
                self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.minimizeBtn = QPushButton(self.frame_7)
                self.minimizeBtn.setObjectName(u"minimizeBtn")
                icon11 = QIcon()
                icon11.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.minimizeBtn.setIcon(icon11)

                self.horizontalLayout_4.addWidget(self.minimizeBtn)

                self.restoreBtn = QPushButton(self.frame_7)
                self.restoreBtn.setObjectName(u"restoreBtn")
                icon12 = QIcon()
                icon12.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.restoreBtn.setIcon(icon12)

                self.horizontalLayout_4.addWidget(self.restoreBtn)

                self.closeBtn = QPushButton(self.frame_7)
                self.closeBtn.setObjectName(u"closeBtn")
                icon13 = QIcon()
                icon13.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
                self.closeBtn.setIcon(icon13)

                self.horizontalLayout_4.addWidget(self.closeBtn)


                self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


                self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

                self.mainBodyContent = QWidget(self.mainBodyContainer)
                self.mainBodyContent.setObjectName(u"mainBodyContent")
                sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                sizePolicy2.setHorizontalStretch(0)
                sizePolicy2.setVerticalStretch(0)
                sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
                self.mainBodyContent.setSizePolicy(sizePolicy2)
                self.mainBodyContent.setMinimumSize(QSize(745, 394))
                font2 = QFont()
                font2.setBold(False)
                font2.setWeight(50)
                self.mainBodyContent.setFont(font2)
                self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
                self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
                self.mainContentsContainer = QWidget(self.mainBodyContent)
                self.mainContentsContainer.setObjectName(u"mainContentsContainer")
                self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
                self.verticalLayout_15.setObjectName(u"verticalLayout_15")
                self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
                self.mainPages.setObjectName(u"mainPages")
                self.page_6 = QWidget()
                self.page_6.setObjectName(u"page_6")
                self.verticalLayout_16 = QVBoxLayout(self.page_6)
                self.verticalLayout_16.setObjectName(u"verticalLayout_16")
                # self.label_10 = QLabel(self.page_6)
                # self.label_10.setObjectName(u"label_10")
                # self.label_10.setFont(font)
                # self.label_10.setAlignment(Qt.AlignCenter)
                # self.verticalLayout_16.addWidget(self.label_10)

                

                # OPEN FILE BUTTON
                self.openFileBtn = QPushButton(self.page_6)
                self.openFileBtn.setFixedSize(QSize(200, 50))
                self.openFileBtn.setObjectName(u"openFileBtn")
                self.openFileBtn.setFont(font)
                self.openFileBtn.setStyleSheet(
                                                        "QPushButton {"
                                                        "   background-color: #343b47;"
                                                        "   color: #fff;"
                                                        "}"
                                                        "QPushButton:hover {"
                                                        "   background-color: #2c313c;"
                                                        "   color: #fff;"
                                                        "}"
                                                        "QPushButton:pressed {"
                                                        "   background-color: #16191d;"
                                                        "   color: #fff;"
                                                        "}"
                                                )
                self.openFileBtn.clicked.connect(self.open_file_dialog)
                self.verticalLayout_16.addWidget(self.openFileBtn)
                self.verticalLayout_16.setAlignment(self.openFileBtn, Qt.AlignCenter)
                

                # GENERATE REPORT BUTTON
                self.generateReportBtn = QPushButton(self.page_6)
                self.generateReportBtn.setFixedSize(QSize(200, 50))
                self.generateReportBtn.setObjectName(u"generateReportBtn")
                self.generateReportBtn.setFont(font)
                self.generateReportBtn.setStyleSheet(
                                                                "QPushButton {"
                                                                "   background-color: #343b47;"
                                                                "   color: #fff;"
                                                                "}"
                                                                "QPushButton:hover {"
                                                                "   background-color: #2c313c;"
                                                                "   color: #fff;"
                                                                "}"
                                                                "QPushButton:pressed {"
                                                                "   background-color: #16191d;"
                                                                "   color: #fff;"
                                                                "}"
                                                        )
                self.generateReportBtn.clicked.connect(self.fill_tables)
                self.verticalLayout_16.addWidget(self.generateReportBtn)
                self.verticalLayout_16.setAlignment(self.generateReportBtn, Qt.AlignCenter)
                self.mainPages.addWidget(self.page_6)

                # SHOW IN MAP BUTTON
                self.showInMapBtn = QPushButton(self.page_6)
                self.showInMapBtn.setFixedSize(QSize(200, 50))
                self.showInMapBtn.setObjectName(u"showInMapBtn")
                self.showInMapBtn.setFont(font)
                self.showInMapBtn.setStyleSheet(
                                                "QPushButton {"
                                                "   background-color: #343b47;"
                                                "   color: #fff;"
                                                "}"
                                                "QPushButton:hover {"
                                                "   background-color: #2c313c;"
                                                "   color: #fff;"
                                                "}"
                                                "QPushButton:pressed {"
                                                "   background-color: #16191d;"

                                                "   color: #fff;"
                                                "}"
                )
                self.planes = []
                self.showInMapBtn.clicked.connect(self.show_in_map)
                self.verticalLayout_16.addWidget(self.showInMapBtn)
                self.verticalLayout_16.setAlignment(self.showInMapBtn, Qt.AlignCenter)
                self.mainPages.addWidget(self.page_6)


                # Create a sub-layout to center the buttons
                self.home_center_layout = QVBoxLayout()
                self.home_center_layout.addWidget(self.openFileBtn)
                self.home_center_layout.addWidget(self.generateReportBtn)
                self.home_center_layout.addWidget(self.showInMapBtn)
                self.home_center_layout.addStretch(1)

                # Set the sub-layout as the central layout
                self.verticalLayout_16.addStretch(1)
                self.verticalLayout_16.addLayout(self.home_center_layout)
                self.verticalLayout_16.addStretch(1)
                self.verticalLayout_16.setAlignment(self.home_center_layout, Qt.AlignCenter)

                ##### AQUI COMENÇA EL NOSTRE CODI de mapes
                self.page_7 = QWidget()
                self.page_7.setObjectName(u"page_7")
                self.verticalLayout_17 = QVBoxLayout(self.page_7)
                self.verticalLayout_17.setObjectName(u"verticalLayout_17")

                # PLAY BUTTON
                self.playBtn = QPushButton(self.page_7)
                self.playBtn.setFixedSize(QSize(30, 30))
                self.playBtn.setIcon(QIcon('icons/play.svg'))
                self.playBtn.setStyleSheet(
                                                "QPushButton {"
                                                "   background-color: #343b47;"
                                                "}"
                                                "QPushButton:hover {"
                                                "   background-color: #2c313c;"
                                                "}"
                                                "QPushButton:pressed {"
                                                "   background-color: #16191d;"
                                                "}"
                                        )
                self.playBtn.clicked.connect(self.play_simulation)

                # PAUSE BUTTON
                self.pauseBtn = QPushButton(self.page_7)
                self.pauseBtn.setFixedSize(QSize(30, 30))
                self.pauseBtn.setIcon(QIcon('icons/pause.svg'))
                self.pauseBtn.setStyleSheet(
                                                "QPushButton {"
                                                "   background-color: #343b47;"
                                                "}"
                                                "QPushButton:hover {"
                                                "   background-color: #2c313c;"
                                                "}"
                                                "QPushButton:pressed {"
                                                "   background-color: #16191d;"
                                                "}"
                                        )
                self.pauseBtn.clicked.connect(self.pause_simulation)

                # STOP BUTTON
                self.stopBtn = QPushButton(self.page_7)
                self.stopBtn.setFixedSize(QSize(30, 30))
                self.stopBtn.setIcon(QIcon('icons/square.svg'))
                self.stopBtn.setStyleSheet(
                                                "QPushButton {"
                                                "   background-color: #343b47;"
                                                "}"
                                                "QPushButton:hover {"
                                                "   background-color: #2c313c;"
                                                "}"
                                                "QPushButton:pressed {"
                                                "   background-color: #16191d;"
                                                "}"
                                        )
                self.stopBtn.clicked.connect(self.stop_simulation)

                # TIME LABEL
                self.timeLabel = QLabel("Simulation Time", self.page_7)
                self.timeLabel.setObjectName(u"timeLabel")
                self.timeLabel.setFont(font)
                self.timeLabel.setStyleSheet(
                                                "QLabel {"
                                                "   color: #838ea2;"
                                                "}"
                                        )

                self.menu_layout = QHBoxLayout()
                self.menu_layout.addWidget(self.playBtn)
                self.menu_layout.addWidget(self.pauseBtn)
                self.menu_layout.addWidget(self.stopBtn)
                self.menu_layout.addStretch(1)
                self.menu_layout.addWidget(self.timeLabel)
                
                self.verticalLayout_17.addLayout(self.menu_layout)
                self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_17.setSpacing(0)

        
                # Get the absolute path to the HTML file
                script_dir = os.path.dirname(os.path.abspath(__file__))
                self.html_path = os.path.join(script_dir, "map.html")

                # Specify the path to the shapefile (.shp) file
                shapefile_path = 'airports/ne_10m_airports.shp'

                # Read the shapefile using geopandas
                airports = gpd.read_file(shapefile_path)

                # Barcelona Airport
                bcn_airport = airports[airports['iata_code'] == 'BCN']
                self.bcn_airport_lat = bcn_airport['geometry'].y.iloc[0]
                self.bcn_airport_lon = bcn_airport['geometry'].x.iloc[0]

                # Create a Folium map
                self.m = folium.Map(location=[self.bcn_airport_lat, self.bcn_airport_lon], zoom_start=12.5)

                # Save the Folium map as an HTML file
                self.m.save(self.html_path)

                # Create a QWebEngineView widget
                self.webview = QWebEngineView(self.page_7)
                self.webview.setMinimumSize(QSize(800, 600))
                self.verticalLayout_17.addStretch(1)
                self.verticalLayout_17.addWidget(self.webview)
                self.verticalLayout_17.addStretch(1)

                # Load the HTML file in the QWebEngineView widget
                self.webview.load(QUrl.fromLocalFile(self.html_path))

                # Start the timer to update plane positions
                #self.timer = QTimer()
                #self.timer.timeout.connect(self.updatePlanePositions)
                #self.timer.start(1000)  # Update every 1 second

                #### AQUI COMENÇA EL NOSTRE CODI de mapes

                self.mainPages.addWidget(self.page_7)
                self.page_8 = QWidget()
                self.page_8.setObjectName(u"page_8")
                self.verticalLayout_18 = QVBoxLayout(self.page_8)
                self.verticalLayout_18.setObjectName(u"verticalLayout_18")


        ### AQUI COMENÇA EL NOSTRE CODI
                self.label_12 = QLabel(self.page_8)
                self.label_12.setObjectName(u"label_12")
                self.label_12.setFont(font)
                self.label_12.setAlignment(Qt.AlignCenter)
                # ADD WIDGET
                self.verticalLayout_18.addWidget(self.label_12)
        
                self.table = QTableWidget(self.page_8)
                self.table21 = QTableWidget(self.page_8)

         ### AQUI ACABA EL NOSTRE CODI

                self.mainPages.addWidget(self.page_8)

                self.verticalLayout_15.addWidget(self.mainPages)



                self.horizontalLayout_8.addWidget(self.mainContentsContainer)

                self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
                self.rightMenuContainer.setObjectName(u"rightMenuContainer")
                self.rightMenuContainer.setMinimumSize(QSize(200, 0))
                self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
                self.verticalLayout_11.setSpacing(0)
                self.verticalLayout_11.setObjectName(u"verticalLayout_11")
                self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
                self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
                self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
                self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
                self.verticalLayout_12.setSpacing(5)
                self.verticalLayout_12.setObjectName(u"verticalLayout_12")
                self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
                self.frame_8 = QFrame(self.rightMenuSubContainer)
                self.frame_8.setObjectName(u"frame_8")
                self.frame_8.setFrameShape(QFrame.StyledPanel)
                self.frame_8.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
                self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
                self.label_7 = QLabel(self.frame_8)
                self.label_7.setObjectName(u"label_7")
                self.label_7.setAlignment(Qt.AlignCenter)

                self.horizontalLayout_9.addWidget(self.label_7)

                self.closeRightMenuBtn = QPushButton(self.frame_8)
                self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
                self.closeRightMenuBtn.setIcon(icon7)
                self.closeRightMenuBtn.setIconSize(QSize(24, 24))

                self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


                self.verticalLayout_12.addWidget(self.frame_8)

                self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
                self.rightMenuPages.setObjectName(u"rightMenuPages")
                self.page_4 = QWidget()
                self.page_4.setObjectName(u"page_4")
                self.verticalLayout_13 = QVBoxLayout(self.page_4)
                self.verticalLayout_13.setObjectName(u"verticalLayout_13")
                self.label_8 = QLabel(self.page_4)
                self.label_8.setObjectName(u"label_8")
                self.label_8.setFont(font)
                self.label_8.setAlignment(Qt.AlignCenter)

                self.verticalLayout_13.addWidget(self.label_8)

                self.rightMenuPages.addWidget(self.page_4)
                self.page_5 = QWidget()
                self.page_5.setObjectName(u"page_5")
                self.verticalLayout_14 = QVBoxLayout(self.page_5)
                self.verticalLayout_14.setObjectName(u"verticalLayout_14")
                self.label_9 = QLabel(self.page_5)
                self.label_9.setObjectName(u"label_9")
                self.label_9.setFont(font)
                self.label_9.setAlignment(Qt.AlignCenter)

                self.verticalLayout_14.addWidget(self.label_9)

                self.rightMenuPages.addWidget(self.page_5)

                self.verticalLayout_12.addWidget(self.rightMenuPages)


                self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


                self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


                self.verticalLayout_10.addWidget(self.mainBodyContent)

                self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
                self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
                self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
                self.verticalLayout_19.setObjectName(u"verticalLayout_19")
                self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
                self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
                self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
                self.verticalLayout_20.setObjectName(u"verticalLayout_20")
                self.label_14 = QLabel(self.popupNotificationSubContainer)
                self.label_14.setObjectName(u"label_14")
                font3 = QFont()
                font3.setBold(True)
                font3.setWeight(75)
                self.label_14.setFont(font3)

                self.verticalLayout_20.addWidget(self.label_14)

                self.frame_9 = QFrame(self.popupNotificationSubContainer)
                self.frame_9.setObjectName(u"frame_9")
                self.frame_9.setFrameShape(QFrame.StyledPanel)
                self.frame_9.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
                self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
                self.label_13 = QLabel(self.frame_9)
                self.label_13.setObjectName(u"label_13")
                sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
                self.label_13.setSizePolicy(sizePolicy1)
                self.label_13.setAlignment(Qt.AlignCenter)

                self.horizontalLayout_10.addWidget(self.label_13)

                self.closeNotificationBtn = QPushButton(self.frame_9)
                self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
                self.closeNotificationBtn.setIcon(icon7)
                self.closeNotificationBtn.setIconSize(QSize(24, 24))

                self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


                self.verticalLayout_20.addWidget(self.frame_9)


                self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


                self.verticalLayout_10.addWidget(self.popupNotificationContainer)

                self.footerContainer = QWidget(self.mainBodyContainer)
                self.footerContainer.setObjectName(u"footerContainer")
                self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
                self.horizontalLayout_11.setSpacing(0)
                self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
                self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
                self.frame_10 = QFrame(self.footerContainer)
                self.frame_10.setObjectName(u"frame_10")
                self.frame_10.setFrameShape(QFrame.StyledPanel)
                self.frame_10.setFrameShadow(QFrame.Raised)
                self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
                self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
                self.label_15 = QLabel(self.frame_10)
                self.label_15.setObjectName(u"label_15")

                self.horizontalLayout_12.addWidget(self.label_15)


                self.horizontalLayout_11.addWidget(self.frame_10)

                self.sizeGrip = QFrame(self.footerContainer)
                self.sizeGrip.setObjectName(u"sizeGrip")
                self.sizeGrip.setMinimumSize(QSize(30, 30))
                self.sizeGrip.setMaximumSize(QSize(30, 30))
                self.sizeGrip.setFrameShape(QFrame.StyledPanel)
                self.sizeGrip.setFrameShadow(QFrame.Raised)

                self.horizontalLayout_11.addWidget(self.sizeGrip)


                self.verticalLayout_10.addWidget(self.footerContainer)


                self.horizontalLayout.addWidget(self.mainBodyContainer)

                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)

                self.centerMenuPages.setCurrentIndex(0)
                self.mainPages.setCurrentIndex(0)
                self.rightMenuPages.setCurrentIndex(0)


                QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

        # Function to handle button click event
        def open_file_dialog(self):
                self.generateReportBtn.setStyleSheet(
                                                                "QPushButton {"
                                                                "   background-color: #343b47;"
                                                                "   color: #fff;"
                                                                "}"
                                                                "QPushButton:hover {"
                                                                "   background-color: #2c313c;"
                                                                "   color: #fff;"
                                                                "}"
                                                                "QPushButton:pressed {"
                                                                "   background-color: #16191d;"
                                                                "   color: #fff;"
                                                                "}"
                                                        )
                self.showInMapBtn.setStyleSheet(
                                                                "QPushButton {"
                                                                "   background-color: #343b47;"
                                                                "   color: #fff;"
                                                                "}"
                                                                "QPushButton:hover {"
                                                                "   background-color: #2c313c;"
                                                                "   color: #fff;"
                                                                "}"
                                                                "QPushButton:pressed {"
                                                                "   background-color: #16191d;"
                                                                "   color: #fff;"
                                                                "}"
                                                        )
                self.file_dialog = QFileDialog()
                self.file_path, _ = self.file_dialog.getOpenFileName(self.page_6, "Open File", "", "All Files (*.*)")
                if self.file_path:
                        self.file = decode(self.file_path)
                        self.label_10 = QLabel(self.page_6)
                        self.label_10.setText(f'FILE OPENED: {self.file_path}')
                        self.label_10.setFont(QFont("Arial", 13, QFont.Bold))
                        self.label_10.setAlignment(Qt.AlignCenter)
                        self.verticalLayout_16.addWidget(self.label_10)
                        self.verticalLayout_16.setAlignment(self.label_10, Qt.AlignLeft)


        # Function to handle button click event     
        def fill_tables(self):
                self.time = 0
                self.x = 0
                self.y = 0
                self.z = 0
                self.FL = 0
                self.plane_id = ""
                self.traffic_type = ""
                

                self.table.setObjectName(u"table")
                self.table21.setObjectName(u"table21")

                self.table.setColumnCount(27)
                

                self.table21.setColumnCount(30)
                

                self.table.setHorizontalHeaderLabels(["Category", 
                                                "SAC", 
                                                "SIC",
                                                "Message Type", 
                                                "Target Report Descriptor", 
                                                "Time of Day", 
                                                "Position in WGS-84 coordinates", 
                                                "Position in polar coordinates", 
                                                "Position in Cartesian coordinates", 
                                                "Calculated Track Velocity in polar coordinates", 
                                                "Calculated Track Velocity in Cartesian coordinates", 
                                                "Track Number", 
                                                "Track Status", 
                                                "Mode-3/A Code in Octal Representation", 
                                                "Target Address", 
                                                "Target Identification", 
                                                "Mode-S MB Data", 
                                                "Vehicle Fleet Identification", 
                                                "Flight Level in Binary Representation", 
                                                "Measured Height", 
                                                "Target Size & Orientation", 
                                                "System Status", 
                                                "Pre-programmed Message", 
                                                "Standard Deviation of Position", 
                                                "Presence", 
                                                "Amplitude of Primary Plot", 
                                                "Calculated Acceleration" ])

                self.table21.setHorizontalHeaderLabels(["Category",
                                                        "SAC",
                                                        "SIC",
                                                        "Target Report Descriptor",
                                                        "Track Number",
                                                        "Service Identification",
                                                        "Time of Applicability for Position",
                                                        "Position in WGS-84 coordinates",
                                                        "Position in WGS-84 coordinates, high res",
                                                        "Time of Applicability for Velocity",
                                                        "Air Speed",
                                                        "True Air Speed",
                                                        "Target Address",
                                                        "Time of Message Reception for Position",
                                                        "Time of Message Reception for Position, high precision",
                                                        "Time of Message Reception for Velocity",
                                                        "Time of Message Reception for Velocity, high precision",
                                                        "Geometric Height",
                                                        "Quality Indicators",
                                                        "MOPS Version",
                                                        "Mode-3/A Code in Octal Representation",
                                                        "Roll Angle",
                                                        "Flight Level in Binary Representation",
                                                        "Magnetic Heading",
                                                        "Target Status",
                                                        "Barometric Vertical Rate",
                                                        "Geometric Vertical Rate",
                                                        "Airborne Ground Vector",
                                                        "Track Angle Rate",
                                                        "Time of Report Transmission for Position",])
                m=0
                row = 1
                row21 = 1
                while m<1000:
                #while m<len(self.file.datablock_list):
                        dataitems_list = self.file.datablock_list[m].record.dataitems_list
                        if self.file.datablock_list[m].cat == 10:
                                self.table.setRowCount(row)
                                row = row + 1
                                n=0
                                while n<len(dataitems_list):
                                        self.table.setItem(m, 0, QTableWidgetItem(f'{self.file.datablock_list[m].cat}')) # Category
                                        if dataitems_list[n].FRN == 1 and dataitems_list[n].dataitem != None: # SAC/SIC
                                                SAC = dataitems_list[n].dataitem.decoded_data[0]
                                                SIC = dataitems_list[n].dataitem.decoded_data[1]
                                                self.table.setItem(m, 1, QTableWidgetItem(f'{SAC}'))
                                                self.table.setItem(m, 2, QTableWidgetItem(f'{SIC}'))
                                                if SIC == 7:
                                                        self.traffic_type = 'SMR'
                                                        lat0=41.295556
                                                        lon0=2.095
                                                        h0=0
                                                elif SIC == 107:
                                                        self.traffic_type = 'MLAT'
                                                        lat0=41.296944
                                                        lon0=2.078333
                                                        h0=0
                                                
                                        elif dataitems_list[n].FRN == 2 and dataitems_list[n].dataitem != None: # Message Type
                                                self.table.setItem(m, 3, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 3 and dataitems_list[n].dataitem != None: # Target Report Descriptor
                                                self.table.setItem(m, 4, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 4 and dataitems_list[n].dataitem != None: # Time of Day
                                                self.table.setItem(m, 5, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                                self.time = dataitems_list[n].dataitem.decoded_data # TIME
                                        elif dataitems_list[n].FRN == 5 and dataitems_list[n].dataitem != None: # Position in WGS-84 coordinates
                                                self.table.setItem(m, 6, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 6 and dataitems_list[n].dataitem != None: # Position in polar coordinates
                                                self.table.setItem(m, 7, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 7 and dataitems_list[n].dataitem != None: # Position in Cartesian coordinates
                                                self.table.setItem(m, 8, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                                self.x = dataitems_list[n].dataitem.decoded_data[0] # X
                                                self.y = dataitems_list[n].dataitem.decoded_data[1] # Y
                                        elif dataitems_list[n].FRN == 8 and dataitems_list[n].dataitem != None: # Calculated Track Velocity in polar coordinates
                                                self.table.setItem(m, 9, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 9 and dataitems_list[n].dataitem != None: # Calculated Track Velocity in Cartesian coordinates
                                                self.table.setItem(m, 10, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 10 and dataitems_list[n].dataitem != None: # Track Number
                                                self.table.setItem(m, 11, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 11 and dataitems_list[n].dataitem != None: # Track Status
                                                self.table.setItem(m, 12, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 12 and dataitems_list[n].dataitem != None: # Mode-3/A Code in Octal Representation
                                                self.table.setItem(m, 13, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 13 and dataitems_list[n].dataitem != None: # Target Address
                                                self.table.setItem(m, 14, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                                self.plane_id = dataitems_list[n].dataitem.decoded_data # PLANE ID
                                        elif dataitems_list[n].FRN == 14 and dataitems_list[n].dataitem != None: # Target Identification
                                                self.table.setItem(m, 15, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 15 and dataitems_list[n].dataitem != None: # Mode-S MB Data
                                                self.table.setItem(m, 16, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 16 and dataitems_list[n].dataitem != None: # Vehicle Fleet Identification
                                                self.table.setItem(m, 17, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 17 and dataitems_list[n].dataitem != None: # Flight Level in Binary Representation
                                                self.table.setItem(m, 18, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                                self.FL = dataitems_list[n].dataitem.decoded_data[2] # FL
                                        elif dataitems_list[n].FRN == 18 and dataitems_list[n].dataitem != None: # Measured Height
                                                self.table.setItem(m, 19, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 19 and dataitems_list[n].dataitem != None: # Target Size & Orientation
                                                self.table.setItem(m, 20, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 20 and dataitems_list[n].dataitem != None: # System Status
                                                self.table.setItem(m, 21, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 21 and dataitems_list[n].dataitem != None: # Pre-programmed Message
                                                self.table.setItem(m, 22, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 22 and dataitems_list[n].dataitem != None: # Standard Deviation of Position
                                                self.table.setItem(m, 23, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 23 and dataitems_list[n].dataitem != None: # Presence
                                                self.table.setItem(m, 24, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 24 and dataitems_list[n].dataitem != None: # Amplitude of Primary Plot
                                                self.table.setItem(m, 25, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}'))
                                        elif dataitems_list[n].FRN == 25 and dataitems_list[n].dataitem != None: # Calculated Acceleration
                                                self.table.setItem(m, 26, QTableWidgetItem(f'{dataitems_list[n].dataitem.decoded_data}')) 
                                        
                                        n=n+1
                                lat, lon, alt = pm.enu2geodetic(self.x, self.y, 0, lat0, lon0, h0, ell = pm.Ellipsoid.from_name('wgs84'), deg=True)
                                self.plane = {
                                        'plane_id': self.plane_id,
                                        'time': self.time,
                                        'lat': lat,
                                        'lon': lon,
                                        'traffic_type': self.traffic_type,
                                        'FL': int(self.FL),
                                        'm': m
                                }
                                self.planes.append(self.plane)
                               
                                
                        elif self.file.datablock_list[m].cat == 21:
                                self.traffic_type = 'ADS-B'
                                self.table21.setRowCount(row21)
                                row21 = row21 + 1
                                k=0
                                while k<len(dataitems_list):
                                        self.table21.setItem(m, 0, QTableWidgetItem(f'{self.file.datablock_list[m].cat}')) # Category
                                        if dataitems_list[k].FRN == 1 and dataitems_list[k].dataitem != None: # SAC/SIC
                                                self.table21.setItem(m, 1, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data[0]}'))
                                                self.table21.setItem(m, 2, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data[1]}'))
                                        elif dataitems_list[k].FRN == 2 and dataitems_list[k].dataitem != None: # Target Report Descriptor
                                                self.table21.setItem(m, 3, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 3 and dataitems_list[k].dataitem != None: # Track Number
                                                self.table21.setItem(m, 4, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 4 and dataitems_list[k].dataitem != None: # Service Identificator
                                                self.table21.setItem(m, 5, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 5 and dataitems_list[k].dataitem != None: # Time of Applicability for Position
                                                self.table21.setItem(m, 6, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 6 and dataitems_list[k].dataitem != None: # Position in WGS-84 coordinates
                                                self.table21.setItem(m, 7, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 7 and dataitems_list[k].dataitem != None: # Position in WGS-84, high res.
                                                self.table21.setItem(m, 8, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                                self.lat = dataitems_list[k].dataitem.decoded_data[0] # LATITUDE
                                                self.lon = dataitems_list[k].dataitem.decoded_data[1] # LONGITUDE
                                        elif dataitems_list[k].FRN == 8 and dataitems_list[k].dataitem != None: # Time of Applicability for Velocity
                                                self.table21.setItem(m, 9, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 9 and dataitems_list[k].dataitem != None: # Airspeed
                                                self.table21.setItem(m, 10, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 10 and dataitems_list[k].dataitem != None: # True Airspeed
                                                self.table21.setItem(m, 11, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 11 and dataitems_list[k].dataitem != None: # Target Address
                                                self.table21.setItem(m, 12, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                                self.plane_id = dataitems_list[k].dataitem.decoded_data # PLANE ID
                                        elif dataitems_list[k].FRN == 12 and dataitems_list[k].dataitem != None: # Time of Message Reception for Position
                                                self.table21.setItem(m, 13, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 13 and dataitems_list[k].dataitem != None: # Time of Message Reception for Position, high precision
                                                self.table21.setItem(m, 14, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 14 and dataitems_list[k].dataitem != None: # Time of Message Reception for Velocity
                                                self.table21.setItem(m, 15, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 15 and dataitems_list[k].dataitem != None: # Time of Message Reception for Velocity, high precision
                                                self.table21.setItem(m, 16, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 16 and dataitems_list[k].dataitem != None: # Geometric Height
                                                self.table21.setItem(m, 17, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 17 and dataitems_list[k].dataitem != None: # Quality Indicators
                                                self.table21.setItem(m, 18, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 18 and dataitems_list[k].dataitem != None: # MOPS Version
                                                self.table21.setItem(m, 19, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 19 and dataitems_list[k].dataitem != None: # Mode-3/A Code in Octal Representation
                                                self.table21.setItem(m, 20, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 20 and dataitems_list[k].dataitem != None: # Roll Angle
                                                self.table21.setItem(m, 21, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 21 and dataitems_list[k].dataitem != None: # Flight Level in Binary Representation
                                                self.table21.setItem(m, 22, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                                self.FL = dataitems_list[k].dataitem.decoded_data # FL
                                        elif dataitems_list[k].FRN == 22 and dataitems_list[k].dataitem != None: # Magnetic Heading
                                                self.table21.setItem(m, 23, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 23 and dataitems_list[k].dataitem != None: # Target Status
                                                self.table21.setItem(m, 24, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 24 and dataitems_list[k].dataitem != None: # Barometric Vertical Rate
                                                self.table21.setItem(m, 25, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 25 and dataitems_list[k].dataitem != None: # Geometric Vertical Rate
                                                self.table21.setItem(m, 26, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 26 and dataitems_list[k].dataitem != None: # Airborne Ground Vector
                                                self.table21.setItem(m, 27, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 27 and dataitems_list[k].dataitem != None: # Track Angle Rate
                                                self.table21.setItem(m, 28, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                        elif dataitems_list[k].FRN == 28 and dataitems_list[k].dataitem != None: # Time of Report Transmission for Position
                                                self.table21.setItem(m, 29, QTableWidgetItem(f'{dataitems_list[k].dataitem.decoded_data}'))
                                                self.time = dataitems_list[k].dataitem.decoded_data # TIME
                                        k=k+1
                                self.plane = {
                                        "plane_id": self.plane_id,
                                        "time": self.time,
                                        "lat": self.lat,
                                        "lon": self.lon,
                                        "traffic_type": self.traffic_type,
                                        "FL": int(self.FL),
                                }
                                self.planes.append(self.plane)
                        else:
                                row21 = row21 + 1
                                        
                        m=m+1
                
                # CAT 10 TABLE
                self.table_title = QLabel(self.page_8)
                self.table_title.setText("CAT 10")
                self.table_title.setFont(QFont("Arial", 13, QFont.Bold))
                self.table_title.setAlignment(Qt.AlignLeft)
                self.verticalLayout_18.addWidget(self.table_title)

                self.table.setShowGrid(True) # Show grid
                self.table.setStyleSheet("QTableView { gridline-color: #343b47; }")
                self.table.resizeColumnsToContents() # Resize columns to contents

                self.table.horizontalHeader().setVisible(True) # Show horizontal header
                self.table.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #16191d; color: #f0f0f0; border: 0.5px solid #16191d; }")
                self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
                self.table.horizontalHeader().setMinimumSectionSize(100) # Set minimum size
                self.table.horizontalHeader().setHighlightSections(True) # Highlight sections
                self.table.horizontalHeader().setSortIndicatorShown(True) # Show sort indicator
                self.table.horizontalHeader().setStretchLastSection(True) # Stretch last section
                

                self.table.verticalHeader().setVisible(True) # Show vertical header
                self.table.verticalHeader().setStyleSheet("QHeaderView::section { background-color: #16191d; color: #f0f0f0; border: 0.5px solid #16191d; }")
                self.table.verticalHeader().setHighlightSections(True) # Highlight sections
                self.table.verticalHeader().setMinimumSectionSize(50) # Set minimum size
                self.table.verticalHeader().setSortIndicatorShown(False) # Show sort indicator
                self.table.verticalHeader().setStretchLastSection(False) # Stretch last section
                
                # Show table
                if self.table.rowCount() > 0:
                        self.table_title.setVisible(True)
                        self.table.setVisible(True)
                else:
                        self.table_title.setVisible(False)
                        self.table.setVisible(False)

                # Fill empty cells with "No Data Available"
                for row in range(self.table.rowCount()):
                        for col in range(self.table.columnCount()):
                                item = self.table.item(row, col)
                                if item is None:
                                        new_item = QTableWidgetItem("NO DATA AVAILABLE")
                                        new_item.setData(Qt.ForegroundRole, QColor(52, 59, 71))
                                        self.table.setItem(row, col, new_item)
                                self.table.item(row,col).setTextAlignment(Qt.AlignCenter)
                self.verticalLayout_18.addWidget(self.table)

                # CAT 21 TABLE
                self.table_title21 = QLabel(self.page_8)
                self.table_title21.setText("CAT 21")
                self.table_title21.setFont(QFont("Arial", 13, QFont.Bold))
                self.table_title21.setAlignment(Qt.AlignLeft)
                self.verticalLayout_18.addWidget(self.table_title21)

                self.table21.setShowGrid(True) # Show grid
                # Set the grid color
                self.table21.setStyleSheet("QTableView { gridline-color: #343b47; }")
                self.table21.resizeColumnsToContents() # Resize columns to contents

                self.table21.horizontalHeader().setVisible(True) # Show horizontal header
                self.table21.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #16191d; color: #f0f0f0; border: 0.5px solid #16191d; }")
                self.table21.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.table21.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
                self.table21.horizontalHeader().setMinimumSectionSize(100) # Set minimum size
                self.table21.horizontalHeader().setHighlightSections(True) # Highlight sections
                self.table21.horizontalHeader().setSortIndicatorShown(True) # Show sort indicator
                self.table21.horizontalHeader().setStretchLastSection(True) # Stretch last section
                

                self.table21.verticalHeader().setVisible(True) # Show vertical header
                self.table21.verticalHeader().setStyleSheet("QHeaderView::section { background-color: #16191d; color: #f0f0f0; border: 0.5px solid #16191d; }")
                self.table21.verticalHeader().setHighlightSections(True) # Highlight sections
                self.table21.verticalHeader().setMinimumSectionSize(50) # Set minimum size
                self.table21.verticalHeader().setSortIndicatorShown(False) # Show sort indicator
                self.table21.verticalHeader().setStretchLastSection(False) # Stretch last section
        
                # Show table
                if self.table21.rowCount() > 0:
                        self.table_title21.setVisible(True)
                        self.table21.setVisible(True)

                else:
                        self.table_title21.setVisible(False)
                        self.table21.setVisible(False)

                # Fill empty cells with "No Data Available"
                for row in range(self.table21.rowCount()):
                        for col in range(self.table21.columnCount()):
                                item = self.table21.item(row, col)
                                if item is None:
                                        new_item = QTableWidgetItem("NO DATA AVAILABLE")
                                        new_item.setData(Qt.ForegroundRole, QColor(52, 59, 71))
                                        self.table21.setItem(row, col, new_item)
                                        self.table21.item(row,col).setTextAlignment(Qt.AlignCenter)
                                
                self.verticalLayout_18.addWidget(self.table21)
                self.generateReportBtn.setStyleSheet("background-color: green;")
                
        
        def show_in_map(self):
                for plane in self.planes:

                        html = f"{plane['traffic_type']}<br>TA: {plane['plane_id']}<br>FL: {plane['FL']}"

                        iframe = folium.IFrame(html,
                        width=100,
                        height=80)

                        
                        
                        if plane['traffic_type']=='SMR':
                                folium.Marker(location=[plane['lat'], plane['lon']], 
                                popup=folium.Popup(plane['traffic_type'], width=70),
                                icon=folium.Icon(color='red', icon='plane', prefix='fa')
                                ).add_to(self.m)
                        elif plane['traffic_type']=='MLAT':
                                folium.Marker(location=[plane['lat'], plane['lon']], 
                                popup=folium.Popup(iframe,max_width=300),
                                icon=folium.Icon(color='green', icon='plane', prefix='fa')
                                ).add_to(self.m)
                        elif plane['traffic_type']=='ADS-B':
                                folium.Marker(location=[plane['lat'], plane['lon']], 
                                popup=folium.Popup(iframe,max_width=300),
                                icon=folium.Icon(color='blue', icon='plane', prefix='fa')
                                ).add_to(self.m)
                # Save the Folium map as an HTML file
                self.m.save(self.html_path)

                # Load the HTML file in the QWebEngineView widget
                self.webview.load(QUrl.fromLocalFile(self.html_path))
                print(self.planes[0])
                self.showInMapBtn.setStyleSheet("background-color: green;")
        
        def play_simulation(self):
                # Timer
                self.timer = QTimer()
                self.timer.setInterval(1000)
                self.timer.timeout.connect(self.update_simulation)
                self.timer.start(1000)
                self.playBtn.setEnabled(False)
                self.pauseBtn.setEnabled(True)
                self.stopBtn.setEnabled(True)
                self.playBtn.setStyleSheet("background-color: grey;")
                self.pauseBtn.setStyleSheet("background-color: green;")
                self.stopBtn.setStyleSheet("background-color: red;")
        
        def pause_simulation(self):
                self.timer.stop()
                self.playBtn.setEnabled(True)
                self.pauseBtn.setEnabled(False)
                self.stopBtn.setEnabled(True)
                self.playBtn.setStyleSheet("background-color: green;")
                self.pauseBtn.setStyleSheet("background-color: grey;")
                self.stopBtn.setStyleSheet("background-color: red;")
                self.timeLabel.setText("Simulation is paused...")
        
        def stop_simulation(self):
                self.timer.stop()
                self.playBtn.setEnabled(True)
                self.pauseBtn.setEnabled(False)
                self.stopBtn.setEnabled(False)
                self.playBtn.setStyleSheet("background-color: green;")
                self.pauseBtn.setStyleSheet("background-color: grey;")
                self.stopBtn.setStyleSheet("background-color: grey;")
                self.timeLabel.setText("Simulation is stopped...")
        
        def update_simulation(self):
                self.current_time = QDateTime.currentDateTime()
                self.timeLabel.setText("Simulation is running... Time: " + str(self.current_time.toString(Qt.ISODate)))
                self.update_map()
        
        def update_map(self):
                # Clear map
                self.m = folium.Map(location=[self.bcn_airport_lat, self.bcn_airport_lon], zoom_start=10)
                self.webview.load(QUrl.fromLocalFile(self.html_path))
                # Print in map markers for planes in current time
                for plane in self.planes:
                        if self.current_time < plane['time'] < self.current_time + 1:
                                html = f"{plane['traffic_type']}<br>TA: {plane['plane_id']}<br>FL: {plane['FL']}"
                                iframe = folium.IFrame(html,
                                width=100,
                                height=80)
                                if plane['traffic_type']=='SMR':
                                        folium.Marker(location=[plane['lat'], plane['lon']], 
                                        popup=folium.Popup(plane['traffic_type'], width=70),
                                        icon=folium.Icon(color='red', icon='plane', prefix='fa')
                                        ).add_to(self.m)
                                elif plane['traffic_type']=='MLAT':
                                        folium.Marker(location=[plane['lat'], plane['lon']], 
                                        popup=folium.Popup(iframe,max_width=300),
                                        icon=folium.Icon(color='green', icon='plane', prefix='fa')
                                        ).add_to(self.m)
                                elif plane['traffic_type']=='ADS-B':
                                        folium.Marker(location=[plane['lat'], plane['lon']], 
                                        popup=folium.Popup(iframe,max_width=300),
                                        icon=folium.Icon(color='blue', icon='plane', prefix='fa')
                                        ).add_to(self.m)
                # Save the Folium map as an HTML file
                self.m.save(self.html_path)
                # Load the HTML file in the QWebEngineView widget
                self.webview.load(QUrl.fromLocalFile(self.html_path))

        def retranslateUi(self, MainWindow):
                MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
                self.openFileBtn.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
                self.generateReportBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Reports", None))
                self.showInMapBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Map View", None))
        #if QT_CONFIG(tooltip)
                self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
        #endif // QT_CONFIG(tooltip)
                self.menuBtn.setText("")
        #if QT_CONFIG(tooltip)
                self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
        #endif // QT_CONFIG(tooltip)
                self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        #if QT_CONFIG(tooltip)
                self.mapBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Map View", None))
        #endif // QT_CONFIG(tooltip)
                self.mapBtn.setText(QCoreApplication.translate("MainWindow", u"Map View", None))
        #if QT_CONFIG(tooltip)
                self.reportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Reports", None))
        #endif // QT_CONFIG(tooltip)
                self.reportBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        #if QT_CONFIG(tooltip)
                self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to settings", None))
        #endif // QT_CONFIG(tooltip)
                self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        #if QT_CONFIG(tooltip)
                self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the app", None))
        #endif // QT_CONFIG(tooltip)
                self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        #if QT_CONFIG(tooltip)
                self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get more help", None))
        #endif // QT_CONFIG(tooltip)
                self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
                self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
        #if QT_CONFIG(tooltip)
                self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
        #endif // QT_CONFIG(tooltip)
                self.closeCenterMenuBtn.setText("")
                self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
                self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
                self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
                self.label_5.setText("")
                self.label_6.setText(QCoreApplication.translate("MainWindow", u"Obelix", None))
                self.notificationBtn.setText("")
        #if QT_CONFIG(tooltip)
                self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
        #endif // QT_CONFIG(tooltip)
                self.moreMenuBtn.setText("")
        #if QT_CONFIG(tooltip)
                self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
        #endif // QT_CONFIG(tooltip)
                self.profileMenuBtn.setText("")
        #if QT_CONFIG(tooltip)
                self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
        #endif // QT_CONFIG(tooltip)
                self.minimizeBtn.setText("")
        #if QT_CONFIG(tooltip)
                self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
        #endif // QT_CONFIG(tooltip)
                self.restoreBtn.setText("")
        #if QT_CONFIG(tooltip)
                self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
        #endif // QT_CONFIG(tooltip)
                self.closeBtn.setText("")
                # self.label_10.setText(QCoreApplication.translate("MainWindow", u"Home", None))
                
                self.label_12.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
                self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        #if QT_CONFIG(tooltip)
                self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
        #endif // QT_CONFIG(tooltip)
                self.closeRightMenuBtn.setText("")
                self.label_8.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
                self.label_9.setText(QCoreApplication.translate("MainWindow", u"More...", None))
                self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
                self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
        #if QT_CONFIG(tooltip)
                self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close notification", None))
        #endif // QT_CONFIG(tooltip)
                self.closeNotificationBtn.setText("")
                self.label_15.setText(QCoreApplication.translate("MainWindow", u"Copyright SkyLink Connections", None))
        # retranslateUi

