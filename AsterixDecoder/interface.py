import sys
sys.path.append("..")
import geopandas as gpd
import os
import folium
from folium import plugins
import pymap3d as pm
import json
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import QWebEngineView

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

from decoder import decode
from geoutils import generateGeoJSON

import numpy as np
import pandas as pd
import geopandas as gpd
import folium
import datetime
import os

def create_geojson_features(df):
        features = []
        
        for _, row in df.iterrows():
                feature = {
                        'type': 'Feature',
                        'geometry': {
                        'type':'Point', 
                        'coordinates':[row['lon'],row['lat']]
                        },
                        'properties': {
                        'time': pd.to_datetime(row['hour'], unit='h').__str__(),
                        'style': {'color' : ''},
                        'icon': 'circle',
                        'iconstyle':{
                                'fillColor': row['fillColor'],
                                'fillOpacity': 0.8,
                                'stroke': 'true',
                                'radius': row['count'] + 5
                        }
                        }
                }
        features.append(feature)
        return features


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                self.simulation_times = []
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
                self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_17.setSpacing(0)

        
                # Get the absolute path to the HTML file
                script_dir = os.path.dirname(os.path.abspath(__file__))
                self.empty_html_path = os.path.join(script_dir, "empty_map.html")
                self.full_html_path = os.path.join(script_dir, "full_map.html")
                self.temp_html_path = os.path.join(script_dir, "temp_map.html")

                # Specify the path to the shapefile (.shp) file
                shapefile_path = 'airports/ne_10m_airports.shp'

                # Read the shapefile using geopandas
                airports = gpd.read_file(shapefile_path)

                # Barcelona Airport
                bcn_airport = airports[airports['iata_code'] == 'BCN']
                self.bcn_airport_lat = bcn_airport['geometry'].y.iloc[0]
                self.bcn_airport_lon = bcn_airport['geometry'].x.iloc[0]

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
        
        # GEOJSONNNNNNN##############################################################################################################


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
                self.table.setObjectName(u"table")
                self.table21.setObjectName(u"table21")

                self.table.setColumnCount(27)
                self.table21.setColumnCount(30)

                self.table.setHorizontalHeaderLabels([
                                                "Category", 
                                                "SAC", 
                                                "SIC", 
                                                "Message Type", 
                                                "Target Report Descriptor", 
                                                "Time of Day",
                                                "Position in WGS-84",
                                                "Position in Polar",
                                                "Position in Cartesian",
                                                "Calculated Track Velocity in Polar",
                                                "Calculated Track Velocity in Cartesian",
                                                "Track Number",
                                                "Track Status",
                                                "Mode-3/A Code in Octal Representation",
                                                "Measured Height",
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
                                                "Calculated Acceleration"])
                
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
                                                        "Time of Report Transmission for Position"])

                data_table = []
                data_table21 = []

                # Set default values for variables used in the loop
                SAC = SIC = lat0 = lon0 = h0 = x = y = None

                self.planes = []
                self.plane_id = 0
                self.time = 0
                self.traffic_type = ""
                self.FL = 0
                
                # Dictionary mapping FRN values to indices in row
                frn_indices = {
                1: (1, 2), 2: (3,), 3: (4,), 4: (5,), 5: (6,), 6: (7,), 7: (8,), 8: (9,),
                9: (10,), 10: (11,), 11: (12,), 12: (13,), 13: (14,), 14: (15,), 15: (16,),
                16: (17,), 17: (18,), 18: (19,), 19: (20,), 20: (21,), 21: (22,), 22: (23,),
                23: (24,), 24: (25,), 25: (26,), 26: (27,)}
                
                # Dictionary mapping FRN values to indices in row21
                frn_indices21 = {
                1: (1, 2), 2: (3,), 3: (4,), 4: (5,), 5: (6,), 6: (7,), 7: (8,), 8: (9,),
                9: (10,), 10: (11,), 11: (12,), 12: (13,), 13: (14,), 14: (15,), 15: (16,),
                16: (17,), 17: (18,), 18: (19,), 19: (20,), 20: (21,), 21: (22,), 22: (23,),
                23: (24,), 24: (25,), 25: (26,), 26: (27,), 27: (28,), 28: (29,), 29: (30,)}
              

                for m, datablock in enumerate(self.file.datablock_list):
                        dataitems_list = datablock.record.dataitems_list
                        

                        if datablock.cat == 10:
                                row = [f'{datablock.cat}'] + [''] * 27


                                for n, dataitem in enumerate(dataitems_list):
                                        # Store frequently accessed values in local variables
                                        decoded_data = dataitem.dataitem.decoded_data if dataitem.dataitem else None
                                        FRN = dataitem.FRN if dataitem.dataitem else None
                                        
                                        # Initialize indices outside the loop
                                        indices = frn_indices.get(FRN, ())
                                        
                                        if FRN == 1 and decoded_data is not None:  # SAC/SIC
                                                SAC = decoded_data[0]
                                                SIC = decoded_data[1]
                                                row[1], row[2] = str(SAC), str(SIC)

                                                if SIC == 7:
                                                        self.traffic_type = 'SMR'
                                                        lat0, lon0, h0 = 41.295556, 2.095, 0
                                                elif SIC == 107:
                                                        self.traffic_type = 'MLAT'
                                                        lat0, lon0, h0 = 41.296944, 2.078333, 0
                                        else:
                                                for index in indices:
                                                        if decoded_data is not None:
                                                                row[index] = str(decoded_data)
                                        
                                        # Update other variables based on FRN
                                        if FRN == 7 and decoded_data is not None:
                                                x, y = decoded_data[0], decoded_data[1]
                                        elif FRN == 10 and decoded_data is not None:
                                                self.plane_id = decoded_data
                                        elif FRN == 19 and decoded_data is not None:
                                                self.FL = decoded_data[0]
                                        elif FRN == 4 and decoded_data is not None:
                                                self.time = decoded_data                                               
                                        

                                self.planes.append({
                                        'plane_id': self.plane_id,
                                        'time': self.time,
                                        'lat': None,
                                        'lon': None,
                                        'traffic_type': self.traffic_type,
                                        'FL': int(self.FL),
                                        'm': m
                                })

                                if len(self.planes) > 0:
                                        self.planes[-1]['lat'], self.planes[-1]['lon'], _ = pm.enu2geodetic(
                                        x, y, 0, lat0, lon0, h0, ell=pm.Ellipsoid.from_name('wgs84'), deg=True
                                        )

                                data_table.append(row)

                        elif datablock.cat == 21:
                                self.traffic_type = 'ADS-B'
                                row21 = [f'{datablock.cat}'] + [''] * 30

                                for k, dataitem in enumerate(dataitems_list):
                                        # Store frequently accessed values in local variables
                                        decoded_data = dataitem.dataitem.decoded_data if dataitem.dataitem else None
                                        FRN = dataitem.FRN if dataitem.dataitem else None
                                        
                                        # Initialize indices outside the loop
                                        indices = frn_indices21.get(FRN, ())
                                        
                                        if FRN == 1 and decoded_data is not None:  # SAC/SIC
                                                SAC = decoded_data[0]
                                                SIC = decoded_data[1]
                                                row21[1], row21[2] = str(SAC), str(SIC)
                                        else:
                                                for index in indices:
                                                        if decoded_data is not None:
                                                                row21[index] = str(decoded_data)
                                        # Update other variables based on FRN
                                        if FRN == 7 and decoded_data is not None:
                                                lat, lon = decoded_data[0], decoded_data[1]
                                        elif FRN == 11 and decoded_data is not None:
                                                self.plane_id = decoded_data
                                        elif FRN == 21 and decoded_data is not None:
                                                self.FL = decoded_data
                                        elif FRN == 28 and decoded_data is not None:
                                                self.time = decoded_data   

                                self.planes.append({
                                        'plane_id': self.plane_id,
                                        'time': self.time,
                                        'lat': lat,
                                        'lon': lon,
                                        'traffic_type': self.traffic_type,
                                        'FL': int(self.FL),
                                        'm': m
                                })

                                data_table21.append(row21)

                self.table.setRowCount(len(data_table))
                self.table21.setRowCount(len(data_table21))

                for i, row_data in enumerate(data_table):
                        for j, value in enumerate(row_data):
                                self.table.setItem(i, j, QTableWidgetItem(value))

                for i, row_data in enumerate(data_table21):
                        for j, value in enumerate(row_data):
                                self.table21.setItem(i, j, QTableWidgetItem(value))

                
                
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
               
                features = []
                self.m = folium.Map(location=[self.bcn_airport_lat, self.bcn_airport_lon], zoom_start=12.5)
                
                # Create a QWebEngineView widget
                self.marker_group = folium.FeatureGroup(name='Markers')     
                
                
                for plane in self.planes:
                        feature = generateGeoJSON(plane)
                        features.append(feature)
                        # html = f"{plane['traffic_type']}<br>TA: {plane['plane_id']}<br>FL: {plane['FL']}"
                        # iframe = folium.IFrame(html,
                        # width=100,
                        # height=80)
                        
                        # if plane['traffic_type']=='SMR':
                        #         self.marker_group.add_child(folium.Marker(location=[plane['lat'], plane['lon']], 
                        #         popup=folium.Popup(plane['traffic_type'], width=70),
                        #         icon=folium.Icon(color='red', icon='plane', prefix='fa')
                        #         ))
                        #         self.marker_group.add_to(self.m)
                        # elif plane['traffic_type']=='MLAT':
                        #         self.marker_group.add_child(folium.Marker(location=[plane['lat'], plane['lon']], 
                        #         popup=folium.Popup(iframe,max_width=300),
                        #         icon=folium.Icon(color='green', icon='plane', prefix='fa')
                        #         ))
                        #         self.marker_group.add_to(self.m)
                        # elif plane['traffic_type']=='ADS-B':
                        #         self.marker_group.add_child(folium.Marker(location=[plane['lat'], plane['lon']], 
                        #         popup=folium.Popup(iframe,max_width=300),
                        #         icon=folium.Icon(color='blue', icon='plane', prefix='fa')
                        #         ))
                        #         self.marker_group.add_to(self.m)
                                
                geojson_data = {
                "type": "FeatureCollection",
                "features": features
                }
                
                with open("data.geojson", "w") as f:
                        json.dump(geojson_data, f)
                        
                with open('data.geojson') as j:
                        data = json.load(j)

                plugins.TimestampedGeoJson(data,
                period="PT1S",
                add_last_point=True,
                min_speed=1,
                max_speed=100,
                ).add_to(self.m)
                
                # Save the Folium map as an HTML file
                self.m.save(self.full_html_path)

                self.webview = QWebEngineView(self.page_7)
                self.webview.setMinimumSize(QSize(800, 600))
                self.verticalLayout_17.addStretch(1)
                self.verticalLayout_17.addWidget(self.webview)
                self.verticalLayout_17.addStretch(1)

                # Load the HTML file in the QWebEngineView widget
                self.webview.load(QUrl.fromLocalFile(self.full_html_path))
                self.showInMapBtn.setStyleSheet("background-color: green;")
        
        
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

