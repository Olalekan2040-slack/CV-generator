from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from PIL import Image as PILImage
import base64
import json

class CVGenerator:
    def __init__(self, data):
        self.data = data
        self.styles = getSampleStyleSheet()
        
    def _create_base64_preview(self, pdf_bytes):
        """Convert PDF first page to base64 image for preview"""
        try:
            # Convert PDF to image using PIL
            images = PILImage.open(BytesIO(pdf_bytes))
            preview_buffer = BytesIO()
            # Convert first page to PNG
            if images.mode == 'RGBA':
                images = images.convert('RGB')
            images.save(preview_buffer, format='PNG')
            # Convert to base64
            preview_base64 = base64.b64encode(preview_buffer.getvalue()).decode()
            return f"data:image/png;base64,{preview_base64}"
        except Exception as e:
            print(f"Preview generation error: {e}")
            return None

    def generate_professional_preview(self):
        """Generate preview for professional template"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        story = self._create_professional_content()
        doc.build(story)
        return self._create_base64_preview(buffer.getvalue())

    def generate_modern_preview(self):
        """Generate preview for modern template"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        story = self._create_modern_content()
        doc.build(story)
        return self._create_base64_preview(buffer.getvalue())

    def generate_creative_preview(self):
        """Generate preview for creative template"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        story = self._create_creative_content()
        doc.build(story)
        return self._create_base64_preview(buffer.getvalue())

    def _create_professional_content(self):
        """Create content for professional template matching the dark blue sidebar design"""
        story = []

        # Define custom styles
        self.styles.add(ParagraphStyle(
            name='SidebarHeader',
            parent=self.styles['Heading2'],
            textColor=colors.white,
            fontSize=14,
            spaceAfter=15,
            spaceBefore=15,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='SidebarContent',
            parent=self.styles['Normal'],
            textColor=colors.white,
            fontSize=10,
            spaceAfter=5,
            fontName='Helvetica'
        ))

        self.styles.add(ParagraphStyle(
            name='MainHeader',
            parent=self.styles['Heading1'],
            textColor=colors.HexColor('#1B2631'),
            fontSize=24,
            spaceAfter=2,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='SubHeader',
            parent=self.styles['Normal'],
            textColor=colors.HexColor('#566573'),
            fontSize=12,
            spaceAfter=15,
            fontName='Helvetica'
        ))

        # Create sidebar content
        sidebar_content = []

        # Profile Image
        if hasattr(self, 'profile_image'):
            img = Image(self.profile_image, width=1.5*inch, height=1.5*inch)
            img_table = Table([[img]], colWidths=[2*inch])
            img_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]))
            sidebar_content.append(img_table)

        # Contact section
        sidebar_content.append(Paragraph('CONTACT', self.styles['SidebarHeader']))
        sidebar_content.append(Paragraph(f"📞 {self.data['phone']}", self.styles['SidebarContent']))
        sidebar_content.append(Paragraph(f"✉ {self.data['email']}", self.styles['SidebarContent']))
        sidebar_content.append(Paragraph(f"📍 {self.data['address']}", self.styles['SidebarContent']))
        if 'website' in self.data:
            sidebar_content.append(Paragraph(f"🌐 {self.data['website']}", self.styles['SidebarContent']))

        # Education section
        sidebar_content.append(Paragraph('EDUCATION', self.styles['SidebarHeader']))
        for edu in zip(self.data.getlist('institution[]'),
                        self.data.getlist('degree[]'),
                        self.data.getlist('eduStartDate[]'),
                        self.data.getlist('eduEndDate[]')):
            sidebar_content.append(Paragraph(f"{edu[2]} - {edu[3]}", self.styles['SidebarContent']))
            sidebar_content.append(Paragraph(edu[0], self.styles['SidebarContent']))
            sidebar_content.append(Paragraph(edu[1], self.styles['SidebarContent']))
            sidebar_content.append(Spacer(1, 5))

        # Skills section
        sidebar_content.append(Paragraph('SKILLS', self.styles['SidebarHeader']))
        skills = self.data['skills'].split(',')
        for skill in skills:
            sidebar_content.append(Paragraph(f"• {skill.strip()}", self.styles['SidebarContent']))

        # Languages section
        if 'language[]' in self.data:
            sidebar_content.append(Paragraph('LANGUAGES', self.styles['SidebarHeader']))
            for lang, level in zip(self.data.getlist('language[]'),
                                    self.data.getlist('languageLevel[]')):
                sidebar_content.append(Paragraph(f"{lang} - {level}", self.styles['SidebarContent']))

        # Create main content
        main_content = []

        # Name and title
        main_content.append(Paragraph(self.data['fullName'], self.styles['MainHeader']))
        main_content.append(Paragraph(self.data['profession'], self.styles['SubHeader']))

        # Profile/Summary
        main_content.append(Paragraph('PROFILE', self.styles['MainHeader']))
        main_content.append(Paragraph(self.data['summary'], self.styles['Normal']))
        main_content.append(Spacer(1, 20))

        # Work Experience
        main_content.append(Paragraph('WORK EXPERIENCE', self.styles['MainHeader']))
        for exp in zip(self.data.getlist('position[]'),
                        self.data.getlist('company[]'),
                        self.data.getlist('workStartDate[]'),
                        self.data.getlist('workEndDate[]'),
                        self.data.getlist('workDescription[]')):
            main_content.append(Paragraph(f"{exp[1]}", self.styles['SubHeader']))
            main_content.append(Paragraph(
                f"{exp[0]} | {exp[2]} - {exp[3]}",
                ParagraphStyle(
                    'JobTitle',
                    parent=self.styles['Normal'],
                    textColor=colors.HexColor('#2E86C1'),
                    fontSize=11,
                    fontName='Helvetica-Bold'
                )
            ))
            main_content.append(Paragraph(exp[4], self.styles['Normal']))
            main_content.append(Spacer(1, 15))

        # References if available
        if 'referenceName[]' in self.data:
            main_content.append(Paragraph('REFERENCES', self.styles['MainHeader']))
            for ref in zip(self.data.getlist('referenceName[]'),
                            self.data.getlist('referenceTitle[]'),
                            self.data.getlist('referenceCompany[]'),
                            self.data.getlist('referenceEmail[]'),
                            self.data.getlist('referencePhone[]')):
                main_content.append(Paragraph(f"{ref[0]}", self.styles['SubHeader']))
                main_content.append(Paragraph(f"{ref[1]} at {ref[2]}", self.styles['Normal']))
                main_content.append(Paragraph(f"Email: {ref[3]}", self.styles['Normal']))
                main_content.append(Paragraph(f"Phone: {ref[4]}", self.styles['Normal']))
                main_content.append(Spacer(1, 10))

        # Create two-column layout
        sidebar_width = 2.5*inch
        main_width = 5*inch

        # Create sidebar with dark blue background
        sidebar = Table(
            [[Paragraph("", self.styles['Normal'])] for _ in sidebar_content],
            colWidths=[sidebar_width]
        )
        sidebar.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#1B2631')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
            ('LEFTPADDING', (0, 0), (-1, -1), 20),
            ('RIGHTPADDING', (0, 0), (-1, -1), 20),
            ('TOPPADDING', (0, 0), (-1, -1), 20),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 20),
        ]))

        # Add content to sidebar and main area
        content_table = Table([
            [
                Table([[content] for content in sidebar_content], colWidths=[sidebar_width]),
                Table([[content] for content in main_content], colWidths=[main_width])
            ]
        ], colWidths=[sidebar_width, main_width])

        content_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#1B2631')),
            ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
            ('LEFTPADDING', (0, 0), (-1, -1), 20),
            ('RIGHTPADDING', (0, 0), (-1, -1), 20),
            ('TOPPADDING', (0, 0), (-1, -1), 20),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 20),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))

        story.append(content_table)
        return story

        def _create_modern_content(self):
            """Create content for modern template"""
            story = []
            
            # Modern header with background color
            header_style = ParagraphStyle(
                'ModernHeader',
                parent=self.styles['Heading1'],
                fontSize=28,
                textColor=colors.white,
                backColor=colors.HexColor('#34495e'),
                alignment=1,
                spaceAfter=30
            )
            
            # Two-column layout
            left_col_width = 2.5*inch
            right_col_width = 5*inch
            
            # Header
            header = Table([[Paragraph(self.data['fullName'], header_style)]], 
                        colWidths=[A4[0]-1*inch])
            header.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#34495e')),
                ('PADDING', (0, 0), (-1, -1), 20),
            ]))
            story.append(header)
            
            # Two-column content
            left_content = []
            right_content = []
            
            # Left column (contact, skills, languages)
            left_content.extend(self._create_modern_sidebar())
            
            # Right column (experience, education)
            right_content.extend(self._create_modern_main_content())
            
            # Combine columns
            content_table = Table([[
                Table(left_content, colWidths=[left_col_width]),
                Table(right_content, colWidths=[right_col_width])
            ]])
            
            story.append(content_table)
            return story

    def _create_creative_content(self):
        """Create content for creative template"""
        story = []
        
        # Creative header with accent colors
        header_style = ParagraphStyle(
            'CreativeHeader',
            parent=self.styles['Heading1'],
            fontSize=32,
            textColor=colors.HexColor('#e74c3c'),
            spaceAfter=5
        )
        
        # Diagonal design element
        diagonal_style = ParagraphStyle(
            'DiagonalStyle',
            parent=self.styles['Normal'],
            textColor=colors.white,
            backColor=colors.HexColor('#e74c3c'),
            alignment=2,
            fontSize=14
        )
        
        story.append(Paragraph(self.data['fullName'], header_style))
        story.append(Paragraph(self.data['profession'], diagonal_style))
        
        # Creative contact info layout
        contact_data = [[
            Paragraph(f"<font color='#e74c3c'>{self.data['email']}</font>", self.styles['Normal']),
            Paragraph(f"<font color='#e74c3c'>{self.data['phone']}</font>", self.styles['Normal']),
            Paragraph(f"<font color='#e74c3c'>{self.data['address']}</font>", self.styles['Normal'])
        ]]
        contact_table = Table(contact_data, colWidths=[2*inch]*3)
        story.append(contact_table)
        
        # Add remaining sections with creative styling...
        return story

    def generate_word_document(self):
        """Generate Word document version of CV"""
        doc = Document()
        
        # Add content based on template
        if self.data['template'] == '1':
            self._add_professional_word_content(doc)
        elif self.data['template'] == '2':
            self._add_modern_word_content(doc)
        else:
            self._add_creative_word_content(doc)
            
        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)
        return buffer

    def generate_pdf_document(self):
        """Generate PDF version of CV"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        
        if self.data['template'] == '1':
            story = self._create_professional_content()
        elif self.data['template'] == '2':
            story = self._create_modern_content()
        else:
            story = self._create_creative_content()
            
        doc.build(story)
        buffer.seek(0)
        return buffer