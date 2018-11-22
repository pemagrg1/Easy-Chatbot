1. Simple
<category>
  <pattern> HELLO </pattern>
  <template>
     Hello! Nice to meet you.
  </template>
</category>



2. Simple with * (anything)
<category>
  <pattern> HELLO * </pattern>
  <template>
     Hello! Nice to meet you.
  </template>
</category>



3. Setting names
<category>
      <pattern>MY NAME IS *</pattern>
      <template>
         <set name="name"><star/></set> is a nice name.
      </template>
</category>

<category>
  <pattern>WHAT IS MY NAME</pattern>
  <template>
     Your name is <get name="name"/>.
  </template>
</category>


4. Asking something/about someone
<category>
   <pattern>DO YOU KNOW WHO * IS?</pattern>
   <template>
      <srai>WHO IS <star/></srai>
   </template>
</category>

6. multiple answer
<category>
    <pattern>Once I *</pattern>
    <template>
        <random>
            <li>Go on.</li>
            <li>Can you be more specific?</li>
            <li>I did not know that.</li>
            <li>Are you telling the truth?</li>
            <li>I don't know what that means.</li>
            <li>Try to tell me that another way.</li>
            <li>What is it?</li>
        </random>
    </template>
</category>

7. setting a category
<category>
  <pattern>SCHOOL</pattern>
  <template>School is an important institution in a child's life.</template>
</category>

<category>
  <pattern>_ SCHOOL</pattern>
  <template>
     <srai>SCHOOL</srai>  #this will call tht upper school pattern
  </template>
</category>

<category>
  <pattern>SCHOOL *</pattern>
  <template>
     <srai>SCHOOL</srai>
  </template>
</category>

<category>
  <pattern>_ SCHOOL *</pattern>
  <template>
     <srai>SCHOOL</srai>
  </template>
</category>

</aiml>
