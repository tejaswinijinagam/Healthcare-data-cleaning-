import matplotlib.pyplot as plt
import seaborn as sns

# Set a professional, modern style for the dashboard panel
sns.set_theme(style="whitegrid")

# Initialize a 2x2 grid panel for the layout
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Healthcare Data Visualization Dashboard', fontsize=18, fontweight='bold', pad=25)

# ----------------------------------------------------
# 1. AGE DISTRIBUTION (Vertical Bar Chart)
# ----------------------------------------------------
age_groups = ['0-18', '19-35', '36-50', '51-65', '65+']
age_counts = [10, 25, 42, 30, 20]

sns.barplot(x=age_groups, y=age_counts, ax=axes[0, 0], palette='viridis')
axes[0, 0].set_title('Age Distribution of Patients', fontsize=13, fontweight='bold', pad=10)
axes[0, 0].set_xlabel('Age Cohorts', fontsize=11)
axes[0, 0].set_ylabel('Number of Patients', fontsize=11)

# Annotate value labels on top of each bar
for i, v in enumerate(age_counts):
    axes[0, 0].text(i, v + 1, str(v), ha='center', va='bottom', fontweight='bold')

# ----------------------------------------------------
# 2. GENDER RATIO (Donut Chart)
# ----------------------------------------------------
gender_labels = ['Female', 'Male']
gender_ratios = [56, 44]
gender_colors = ['#4285F4', '#EA4335'] # Match the blue/red UI layout markers

axes[0, 1].pie(gender_ratios, labels=gender_labels, autopct='%1.0f%%', startangle=90, 
               colors=gender_colors, textprops={'fontsize': 11, 'weight': 'bold'}, pctdistance=0.75)
# Draw center white circle to turn the pie chart into a crisp donut chart
centre_circle = plt.Circle((0,0), 0.55, fc='white')
axes[0, 1].add_artist(centre_circle)
axes[0, 1].set_title('Patient Gender Ratio Breakdown', fontsize=13, fontweight='bold', pad=10)

# ----------------------------------------------------
# 3. PATIENTS BY DISEASE (Horizontal Bar Chart)
# ----------------------------------------------------
diseases = ['Hypertension', 'Diabetes']
disease_counts = [40, 30]

sns.barplot(x=disease_counts, y=diseases, ax=axes[1, 0], palette='crest', orient='h')
axes[1, 0].set_title('Volume of Patients by Disease Case', fontsize=13, fontweight='bold', pad=10)
axes[1, 0].set_xlabel('Total Diagnosed Patients', fontsize=11)

# Annotate value labels next to the horizontal bars
for i, v in enumerate(disease_counts):
    axes[1, 0].text(v + 0.5, i, str(v), va='center', ha='left', fontweight='bold')

# ----------------------------------------------------
# 4. MEDICATION USAGE (Pie Chart Distribution)
# ----------------------------------------------------
medications = ['Paracetamol', 'Other Treatments']
med_shares = [15, 85] # 15% Paracetamol segment extracted from image indicator
med_colors = ['#34A853', '#E0E0E0']

axes[1, 1].pie(med_shares, labels=medications, autopct='%1.0f%%', startangle=140, 
               colors=med_colors, textprops={'fontsize': 11, 'weight': 'bold'}, explode=(0.05, 0))
axes[1, 1].set_title('Medication Usage Share', fontsize=13, fontweight='bold', pad=10)

# Final formatting logic adjustments and export step
plt.tight_layout()
plt.savefig('healthcare_visualizations.png', dpi=300, bbox_inches='tight')
print("Successfully generated: 'healthcare_visualizations.png'!")
                    
